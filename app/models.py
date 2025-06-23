from pydantic import RootModel, BaseModel
from typing import Any, Dict


class Payload(RootModel[Dict[str, Any]]):
    """A model whose entire value is an arbitrary dict."""

    pass


class ResponseModel(BaseModel):
    Status: int
    Data: Dict[str, str]
