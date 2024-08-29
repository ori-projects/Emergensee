from pydantic import BaseModel

class CreateAccountRequest(BaseModel):
    email: str
    username : str
    password: str
    role: str