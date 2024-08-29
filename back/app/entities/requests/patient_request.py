from typing import Any, Optional
from fastapi import UploadFile
from pydantic import BaseModel, conbytes

class PatientRequest(BaseModel):
    name: str
    age: int
    email: str
    doctor_id: str
    image: str 
    phone_number: str
