from fastapi import FastAPI, WebSocket
from .routers import budget
import openai

# OpenAI API key; remember to keep this secure in production.
openai.api_key = 'OPENAI_API_KEY'

app = FastAPI()

# Include the routers for budget
app.include_router(budget.router)

@app.websocket("/ws")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()

        # Interact with OpenAI's API
        try:
            response = openai.Completion.create(
              engine="davinci", 
              prompt=data,  # The text/question received via WebSocket
              max_tokens=150  # Adjust parameters as needed
            )
            answer = response.choices[0].text.strip()

            # Send back the AI's response
            await websocket.send_text(answer)
        except Exception as e:
            await websocket.send_text(str(e))
