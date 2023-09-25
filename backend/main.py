from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from routers import budget, user 
import openai
from database.database import engine, SessionLocal
from database.base import Base 
import os

import logging
# OpenAI API key; remember to keep this secure in production.
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

Base.metadata.create_all(bind=engine)
logging.basicConfig(level=logging.INFO)


@app.on_event("startup")
def startup_event():
    logging.info("FastAPI app has started")
    session = SessionLocal()
    # More startup logic here
    session.close()

@app.on_event("shutdown")
def shutdown_event():
    session = SessionLocal()
    # More shutdown logic here
    session.close()


# Include the routers
app.include_router(budget.router, prefix="/budget", tags=["budget"])
app.include_router(user.router, prefix="/users", tags=["users"])  # <-- Include the user router

@app.websocket("/ws")
async def chat_endpoint(websocket: WebSocket):
    log.info("WS Code Called")
    await websocket.accept()
    log.info("WebSocket Accepted")
    
    try:
        while True:
            data = await websocket.receive_text()
            logging.info(f"Received data: {data}")
            
            try:
                # Interact with OpenAI's API
                # response = openai.Completion.create(
                #   engine="davinci", 
                #   prompt=data,  # The text/question received via WebSocket
                #   max_tokens=150  # Adjust parameters as needed
                # )
                # answer = response.choices[0].text.strip()

                # Send back the AI's response
                await websocket.send_text("aint no way")
            except Exception as e:
                logging.error(f"Error interacting with OpenAI: {str(e)}")
                await websocket.send_text(str(e))
    except WebSocketDisconnect:
        logging.info("WebSocket Disconnected")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")