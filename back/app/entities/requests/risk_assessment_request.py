from typing_extensions import Annotated
from pydantic import BaseModel, constr, conint

class RiskAssessmentRequest(BaseModel):
    # Name of the patient, constrained to be between 1 and 100 characters
    name: Annotated[str, constr(min_length=1, max_length=100)]
    
    # Email address of the patient
    email: Annotated[str, constr]
    
    # Phone number of the patient
    phoneNumber: Annotated[str, constr]
    
    # Age of the patient
    age: Annotated[str, constr]
    
    # Blood pressure of the patient
    bloodPressure: Annotated[str, constr]
    
    # Blood sugar level of the patient
    bloodSugar: Annotated[str, constr]
    
    # Number of procedures the patient has undergone
    procedureCount: Annotated[str, constr]
    
    # Number of infections reported by the patient
    infectionsReported: Annotated[str, constr]
    
    # Body temperature of the patient
    bodyTemperature: Annotated[str, constr]
    
    # Heart rate of the patient
    heartRate: Annotated[str, constr]
    
    # Type of operative procedure the patient has undergone
    operativeProcedure: Annotated[str, constr]
    
    # Patient's feelings and urges
    feelingsAndUrge: Annotated[str, constr]
    
    # Disease affecting the patient
    disease: Annotated[str, constr]
    
    # Rating of critical feelings experienced by the patient (0 to 5)
    criticalFeelings: Annotated[str, constr]
    
    # Rating of the disease severity (0 to 5)
    diseaseRating: Annotated[int, conint(ge=0, le=5)]
    
    # Rating related to chronic kidney disease (0 to 5)
    ckdRating: Annotated[int, conint(ge=0, le=5)]
    
    # Rating related to systemic inflammatory response syndrome (0 to 5)
    sirRating: Annotated[int, conint(ge=0, le=5)]
    
    # Rating related to malignancy (0 to 5)
    maRating: Annotated[int, conint(ge=0, le=5)]