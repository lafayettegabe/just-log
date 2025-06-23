from pydantic import BaseModel
from typing import Any, Dict


class Payload(BaseModel):
    __root__: Dict[str, Any]


class ResponseModel(BaseModel):
    Status: int
    Data: Dict[str, str]
