from pydantic import BaseModel

class DeleteAccountRequest(BaseModel):
    id: int
    email: str
    name : str
    password: str
    role: int