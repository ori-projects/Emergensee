import sys
import os
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd  
from app.services.utils.tools import filter_test_columns, process_and_append_cass_data, process_and_append_ckd_data, process_and_append_disease_data, process_and_append_maternal_data, split_dataset
from app.entities.datasets.disease import Disease
from app.entities.datasets.ckd import Ckd
from app.entities.datasets.cassi import Cassi
from app.entities.datasets.maternal import Maternal
from app.interfaces.controller import Controller

# Add parent directory to sys.path to ensure relative imports work correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ToolsController(Controller):
    """
    Controller class for managing tools-related functionalities through FastAPI.
    """

    _instance = None

    @classmethod
    def get_app(cls):
        """
        Singleton method to get or create an instance of the FastAPI application.

        Returns:
        FastAPI: An instance of the FastAPI application.
        """
        if cls._instance is None:
            cls._instance = cls._create_instance()
        return cls._instance

    @classmethod
    def _create_instance(cls):
        """
        Private method to create a new instance of the FastAPI application.

        Returns:
        FastAPI: A new instance of the FastAPI application.
        """
        app = FastAPI(debug=True)

        # Configure CORS middleware for cross-origin requests
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
        )

        # Endpoint to test cass dataset
        @app.post("/test-cass", tags=["Controller Tools"], summary="Test cass")
        def test_cass_controller():
            """
            Endpoint to test cass dataset.

            Returns:
            JSONResponse: A JSON response indicating the success of the operation.
            """
            # 1. Load the CSV
            cassi = Cassi()
            df = cassi.df_raw

            # 2. Split the dataset
            split_ratio = 0.8  # 80% train, 20% test
            test_df = split_dataset(df, split_ratio)

            # 3. Filter test columns
            columns_to_keep = ['Operative_Procedure', 'Procedure_Count', 'Infections_Reported', 'Infections_Predicted', 'SIR']
            df = filter_test_columns(test_df, columns_to_keep)

            # Pass the processed DataFrame to the second function
            return process_and_append_cass_data(cassi, df)

        # Endpoint to test maternal dataset
        @app.post("/test-maternal", tags=["Controller Tools"], summary="Test maternal")
        def test_maternal_controller():
            """
            Endpoint to test maternal dataset.

            Returns:
            JSONResponse: A JSON response indicating the success of the operation.
            """
            # 1. Load the CSV
            maternal = Maternal()
            df = maternal.df_raw

            # 2. Split the dataset
            split_ratio = 0.8  # 80% train, 20% test
            test_df = split_dataset(df, split_ratio)

            # 3. Filter test columns
            columns_to_keep = ['Age', 'SystolicBP', 'BS', 'BodyTemp', 'HeartRate', 'RiskLevel']
            df = filter_test_columns(test_df, columns_to_keep)

            # Pass the processed DataFrame to the second function
            return process_and_append_maternal_data(maternal, df)

        # Endpoint to test ckd dataset
        @app.post("/test-ckd", tags=["Controller Tools"], summary="Test ckd")
        def test_ckd_controller():
            """
            Endpoint to test ckd dataset.

            Returns:
            JSONResponse: A JSON response indicating the success of the operation.
            """
            # 1. Load the CSV
            ckd = Ckd()
            df = ckd.df_raw

            # 2. Split the dataset
            split_ratio = 0.8  # 80% train, 20% test
            test_df = split_dataset(df, split_ratio)

            # 3. Filter test columns
            columns_to_keep = ['age', 'bp', 'bgr', 'ckd']
            df = filter_test_columns(test_df, columns_to_keep)

            # Pass the processed DataFrame to the second function
            return process_and_append_ckd_data(ckd, df)

        # Endpoint to test disease dataset
        @app.post("/test-disease", tags=["Controller Tools"], summary="Test disease")
        def test_disease_controller():
            """
            Endpoint to test disease dataset.

            Returns:
            JSONResponse: A JSON response indicating the success of the operation.
            """
            # 1. Load the CSV
            disease = Disease()
            df = disease.df_raw

            # 2. Split the dataset
            split_ratio = 0.95  # 95% train, 5% test
            test_df = split_dataset(df, split_ratio)

            # 3. Filter test columns
            columns_to_keep = ['Feelings_and_Urge', 'Critical_Feelings', 'Disease', 'Critical']
            df = filter_test_columns(test_df, columns_to_keep)

            # Pass the processed DataFrame to the second function
            return process_and_append_disease_data(disease, df)

        # Endpoint to create test files
        @app.post("/make-test-files", tags=["Controller Tools"], summary="Make test files")
        def get_test_files():
            """
            Endpoint to create test files.

            Returns:
            JSONResponse: A JSON response indicating the success of the operation.
            """
            # Example implementation
            df = pd.read_csv(r'Datasets\\Test\\diabetes.csv')

            columns_to_keep = ['BloodPressure','Age','Diabetes'] # Diabetes DS

            df = filter_test_columns(df, columns_to_keep)
            df.to_csv('Diabetes.csv', index=False)

            df = pd.read_csv(r'Datasets\\Test\\disease_symptom_and_patient_profile.csv')

            columns_to_keep = ['Disease','Fever','Cough','Fatigue','Difficulty Breathing','Age','Blood Pressure','Outcome'] # Disease_symptom_and_patient_profile DS

            df = filter_test_columns(df, columns_to_keep)
            df.to_csv('Disease_symptom_and_patient_profile.csv', index=False)

            df = pd.read_csv(r'Datasets\\Test\\heart_attack.csv')

            columns_to_keep = ['age','pressurehight','class'] # Heart_attack DS

            df = filter_test_columns(df, columns_to_keep)
            df.to_csv('Heart_attack.csv', index=False)

            return JSONResponse(content={"message": "Done"})

        # Endpoint to test the test files
        @app.post("/test-files", tags=["Controller Tools"], summary="Test the test files")
        def test_files():
            """
            Endpoint to test the test files.

            Returns:
            JSONResponse: A JSON response indicating the success of the operation.
            """
            disease = Disease()
            ckd = Ckd()
            cassi = Cassi()
            maternal = Maternal()

            # Example implementation of processing test files
            df = pd.read_csv(r'Heart_attack.csv')
            df.rename(columns={'age': 'Infections_Reported', 
                               'pressurehight': 'Procedure_Count', 
                               'class': 'SIR'}, inplace=True)
            df['Operative_Procedure'] = None
            process_and_append_cass_data(cassi, df, 'Heart_attack.csv') 

            df = pd.read_csv(r'Heart_attack.csv')
            df.rename(columns={'age': 'age', 
                               'pressurehight': 'bp', 
                               'class': 'ckd'}, inplace=True)
            df['bgr'] = None
            process_and_append_ckd_data(ckd, df, 'Heart_attack.csv') 

            df = pd.read_csv(r'Heart_attack.csv')
            df.rename(columns={'class': 'Critical'}, inplace=True)
            df['Critical_Feelings'] = None 
            df['Feelings_and_Urge'] = None 
            df['Disease'] = None
            process_and_append_disease_data(disease, df, 'Heart_attack.csv') 

            df = pd.read_csv(r'Heart_attack.csv')
            df.rename(columns={'age': 'Age', 
                               'pressurehight': 'SystolicBP', 
                               'class': 'RiskLevel'}, inplace=True)
            df['BodyTemp'] = None
            df['HeartRate'] = None
            df['BS'] = None
            process_and_append_maternal_data(maternal, df, 'Heart_attack.csv')

            return JSONResponse(content={"message": "Done"})

        # Endpoint for health check
        @app.get("/health", tags=["Health Check"], summary="Health Check")
        def health_check():
            """
            Health check endpoint to verify the service is running.

            Returns:
            dict: A dictionary indicating the health status of the service.
            """
            return {"status": "ok", "message": "Service is up and running"}

        return app