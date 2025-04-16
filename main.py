from fastapi import FastAPI, Request
import logging
import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/")
async def receive_data(request: Request):
    body = await request.json()
    logger.info(f"Received data: {body}")
    return {"status": "success", "message": "Data received and logged"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)