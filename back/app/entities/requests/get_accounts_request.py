from typing_extensions import Annotated
from pydantic import BaseModel, conint

class GetAccountsRequest(BaseModel):
    id: int
