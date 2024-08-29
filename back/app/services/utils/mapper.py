import math

class Mapper:
    _instance = None

    def __new__(cls):
        """
        Singleton implementation ensuring only one instance of Mapper exists.

        Returns:
        Mapper: The singleton instance of Mapper class.
        """
        if cls._instance is None:
            cls._instance = super(Mapper, cls).__new__(cls)
        return cls._instance
    
    def map_to_ckd_row(json):
        """
        Maps JSON data to a row format suitable for Chronic Kidney Disease (CKD).

        Args:
        json (dict): Input JSON containing data to map.

        Returns:
        dict: Mapped row for CKD dataset.
        """
        return {
            "age": int(json.get("Age", None)) if json.get("Age") is not None else None,
            "bp": int(json.get("Blood Pressure", None)) if json.get("Blood Pressure") is not None else None,
            "sg": None,
            "al": None,
            "su": None,
            "rcb": None,
            "pc": None,
            "pcc": None,
            "ba": None,
            "bgr": int(json.get("Blood Sugar", None)) if json.get("Blood Sugar") is not None else None,
            "bu": None,
            "sc": None,
            "sod": None,
            "pot": None,
            "hemo": None,
            "pcv": None,
            "wbcc": None,
            "rbcc": None,
            "htn": None,
            "dm": None,
            "cad": None,
            "appet": None,
            "pe": None,
            "ane": None,
        }

    def map_to_disease_row(json):
        """
        Maps JSON data to a row format suitable for Disease dataset.

        Args:
        json (dict): Input JSON containing data to map.

        Returns:
        dict: Mapped row for Disease dataset.
        """
        return {
            "Discharge": None,
            "Feelings_and_Urge": json.get("Feelings_and_Urge", None),
            "Pain_and_Infection": None,
            "Physical_Conditions": None,
            "Critical_Feelings": json.get("Critical_Feelings", None),
            "Disease": json.get("Disease", None),
        }

    def map_to_maternal_row(json):
        """
        Maps JSON data to a row format suitable for Maternal dataset.

        Args:
        json (dict): Input JSON containing data to map.

        Returns:
        dict: Mapped row for Maternal dataset.
        """
        return {
            "Age": json.get("Age", None),
            "SystolicBP": json.get("Blood Pressure", None),
            "DiastolicBP": None,
            "BS": json.get("Blood Sugar", None),
            "BodyTemp": json.get("Body Temperature", None),
            "HeartRate": json.get("Heart Rate", None),
        }

    def map_to_cassi_row(json):
        """
        Maps JSON data to a row format suitable for Cassi dataset.

        Args:
        json (dict): Input JSON containing data to map.

        Returns:
        dict: Mapped row for Cassi dataset.
        """
        return {
            "SIR_CI_95_Lower_Limit": None,
            "SIR_CI_95_Upper_Limit" : None,
            "SIR_2015" : None,
            "Operative_Procedure": json.get("Operative_Procedure", None),
            "Infections_Reported": json.get("Infections Reported", None),
            "Infections_Predicted": None,
            "Procedure_Count": json.get("Procedure Count", None),
        }
    
    def map_to_ds_row(ds, row_to_process):
        """
        Maps a row to a dataset format using a provided dataset object.

        Args:
        ds (Dataset): Dataset object used for mapping.
        row_to_process (dict): Row to be processed and mapped.

        Returns:
        dict: Mapped row in dataset format.
        """
        return ds.preprocess_row(row_to_process)
    
    def map_to_risk_assessment_request(self, data):
        """
        Maps data attributes to a format suitable for risk assessment request.

        Args:
        data (object): Object containing attributes related to risk assessment.

        Returns:
        dict: Mapped data attributes for risk assessment.
        """
        return {
            "Age": int(data.age) if data.age and data.age.strip() else None,
            "Blood Pressure": int(data.bloodPressure) if data.bloodPressure and data.bloodPressure.strip() else None,
            "Blood Sugar": int(data.bloodSugar) if data.bloodSugar and data.bloodSugar.strip() else None,
            "Procedure Count": int(data.procedureCount) if data.procedureCount and data.procedureCount.strip() else None,
            "Infections Reported": int(data.infectionsReported) if data.infectionsReported and data.infectionsReported.strip() else None,
            "Body Temperature": int(data.bodyTemperature) if data.bodyTemperature and data.bodyTemperature.strip() else None,
            "Heart Rate": int(data.heartRate) if data.heartRate and data.heartRate.strip() else None,
            "Operative_Procedure": data.operativeProcedure,
            "Feelings_and_Urge": data.feelingsAndUrge,
            "Critical_Feelings": data.criticalFeelings,
            "Disease": data.disease,
            "SIR_Weight": int(data.sirRating) if data.sirRating else 0,
            "MA_Weight": int(data.maRating) if data.maRating else 0,
            "Disease_Weight": int(data.diseaseRating) if data.diseaseRating else 0,
            "CKD_Weight": int(data.ckdRating) if data.ckdRating else 0
        }

    
    def fill_empty_values(input_row, row_nearest_neighbor):
        """
        Fills empty values in an input row using corresponding values from a nearest neighbor row.

        Args:
        input_row (dict): Input row with potentially empty values.
        row_nearest_neighbor (dict): Nearest neighbor row containing corresponding values.

        Returns:
        dict: Completed row with filled empty values.
        """
        completed_row = {}
        for key in input_row:
            if input_row[key] is None or isinstance(input_row[key], float) and math.isnan(input_row[key]):
                completed_row[key] = row_nearest_neighbor.get(key, None) # IF EMPTY AND OTHER HAS VALUE PUT THE VALUE
            else:
                completed_row[key] = input_row[key] # IF NOT EMPTY JUST TAKE THE INPUT

        return completed_row