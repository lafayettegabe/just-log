from fastapi import APIRouter
from .models import Payload, ResponseModel
from .logger import logger_dependency

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.post("/", response_model=ResponseModel)
async def receive_data(payload: Payload, logger: logger_dependency):
    logger.info("Received data: %s", payload.root)
    return ResponseModel(Status=0, Data={"message": "Data received and logged"})
