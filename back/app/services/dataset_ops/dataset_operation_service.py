import math
import time
from app.entities.datasets.cassi import Cassi
from app.entities.datasets.ckd import Ckd
from app.entities.datasets.disease import Disease
from app.entities.datasets.maternal import Maternal
from app.services.risk_assessments.risk_assessments import RiskAssessments
from app.services.utils.datasets_tools import DatasetsTools
from app.services.utils.mapper import Mapper

class DatasetOperationService:
    # Configuration to enable or disable datasets
    CONFIG = {
        "Disease": True,
        "CKD": True,
        "CASSI": True,
        "MaternalHealth": True
    }

    @staticmethod
    def preprocess_datasets():
        """
        Preprocesses enabled datasets.

        Returns:
        str: Success message with the time taken for preprocessing.
        """
        start_time = time.time()

        datasets_instance = DatasetsTools.get_instance()
        datasets = datasets_instance.get_datasets_instances()
        
        for dataset in datasets:
            dataset_name = type(dataset).__name__
            if DatasetOperationService.CONFIG.get(dataset_name, False):
                dataset.preprocess()

        end_time = time.time()
        return f"Success: Preprocess datasets completed. Time taken: {end_time - start_time} seconds."
    
    @staticmethod
    def process_datasets():
        """
        Processes enabled datasets.

        Returns:
        str: Success message with the time taken for processing.
        """
        start_time = time.time()
        
        datasets_instance = DatasetsTools.get_instance()
        datasets = datasets_instance.get_datasets_instances()
    
        for dataset in datasets:
            dataset_name = type(dataset).__name__
            if DatasetOperationService.CONFIG.get(dataset_name, False):
                dataset.process()

        end_time = time.time()
        return f"Success: Process datasets completed. Time taken: {end_time - start_time} seconds."

    @staticmethod
    def get_risk_assessment(input):
        """
        Calculates risk assessment based on enabled datasets and input weights.

        Args:
        input (dict): Input data containing weights for each dataset.

        Returns:
        float: Calculated risk assessment score.
        """
        def predict_risk(ds, input_row, k=5):
            """
            Predicts risk using the given dataset instance and input data.

            Args:
            ds (Dataset): Dataset instance for prediction.
            input_row (dict): Input data row to predict risk for.
            k (int, optional): Number of nearest neighbors to consider. Defaults to 5.

            Returns:
            float: Predicted risk value.
            """
            k_nearest_rows = datasets_tools.find_nearest_rows(ds, input_row, k)
            row_to_predict = Mapper.fill_empty_values(input_row, k_nearest_rows)
            row_to_predict = Mapper.map_to_ds_row(ds, row_to_predict)
            return ds.predict(row_to_predict)
        
        def get_relative_weights(weights, method='linear'):
            """
            Calculates relative weights based on the provided method.

            Args:
            weights (list of float): List of weights for different datasets.
            method (str, optional): Method for calculating relative weights ('linear' or 'square'). Defaults to 'linear'.

            Returns:
            list of float: List of relative weights.
            
            Raises:
            ValueError: If an invalid method is provided.
            """
            total_sum = sum(weights)
            if total_sum == 0:
                return [0] * len(weights)

            if method == 'linear':
                relative_weights = [weight / total_sum for weight in weights]
            elif method == 'square':
                sqrt_weights = [math.sqrt(weight) for weight in weights]
                total_sqrt = sum(sqrt_weights)
                relative_weights = [sqrt_weight / total_sqrt for sqrt_weight in sqrt_weights]
            else:
                raise ValueError("Invalid method. Please choose 'linear' or 'square'.")

            return relative_weights
        
        def multiply_fractions_with_ratio(rows_weight, user_weight, P=0.25):
            """
            Multiplies fractions with ratio to calculate weighted result.

            Args:
            rows_weight (float): Weight of dataset rows.
            user_weight (float): Weight of user input.
            P (float, optional): Proportion factor. Defaults to 0.25.

            Returns:
            float: Weighted result.
            """
            weight1 = P
            weight2 = 1 - P

            result_numerator_linear = (rows_weight * weight1) + (user_weight * weight2)
            result = result_numerator_linear

            return result
        
        # Initialize datasets
        datasets = {
            "Disease": Disease() if DatasetOperationService.CONFIG["Disease"] else None,
            "CKD": Ckd() if DatasetOperationService.CONFIG["CKD"] else None,
            "CASSI": Cassi() if DatasetOperationService.CONFIG["CASSI"] else None,
            "MaternalHealth": Maternal() if DatasetOperationService.CONFIG["MaternalHealth"] else None,
        }

        # Get weights from input
        weights = [
            input.get("Disease_Weight") if datasets["Disease"] else 0,
            input.get("CKD_Weight") if datasets["CKD"] else 0,
            input.get("SIR_Weight") if datasets["CASSI"] else 0,
            input.get("MA_Weight") if datasets["MaternalHealth"] else 0,
        ]
        
        # Calculate relative weights
        relative_weights = get_relative_weights(weights)

        # Initialize results and weights lists
        results = {}
        weights = []
        
        # Get datasets tools instance
        datasets_tools = DatasetsTools.get_instance()

        # Process each enabled dataset and calculate risk
        if datasets["Disease"]:
            disease_weight = multiply_fractions_with_ratio(datasets["Disease"].risk_weight, relative_weights[0])
            disease_row = Mapper.map_to_disease_row(input)
            disease_risks = predict_risk(datasets["Disease"], disease_row)
            results["Probability of patient in Critical Condition per Disease dataset"] = disease_risks
            weights.append(disease_weight)
        
        if datasets["CKD"]:
            ckd_weight = multiply_fractions_with_ratio(datasets["CKD"].risk_weight, relative_weights[1])
            ckd_row = Mapper.map_to_ckd_row(input)
            ckd_risks = predict_risk(datasets["CKD"], ckd_row)
            results["Probability of patient having Chronic Kidney Disease per CKD dataset"] = ckd_risks
            weights.append(ckd_weight)
        
        if datasets["CASSI"]:
            cassi_weight = multiply_fractions_with_ratio(datasets["CASSI"].risk_weight, relative_weights[2])
            cassi_row = Mapper.map_to_cassi_row(input)
            cassi_risks = predict_risk(datasets["CASSI"], cassi_row)
            results["Probability of patient having new infections per CASSI Adult ODP 2022 dataset"] = cassi_risks
            weights.append(cassi_weight)
        
        if datasets["MaternalHealth"]:
            maternal_weight = multiply_fractions_with_ratio(datasets["MaternalHealth"].risk_weight, relative_weights[3])
            maternal_row = Mapper.map_to_maternal_row(input)
            maternal_risks = predict_risk(datasets["MaternalHealth"], maternal_row)
            results["Patient's risk level per Maternal Health Risk dataset"] = maternal_risks
            weights.append(maternal_weight)

        # Calculate final risk assessment score
        score = RiskAssessments.calculate_risk_assessment(results, weights)
        return score