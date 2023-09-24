from fastapi import FastAPI, WebSocket, Depends
import openai

# OpenAI API key; 
openai.api_key = ''

app = FastAPI()

@app.websocket("/ws")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()

        # Interact with OpenAI's API
        try:
            response = openai.Completion.create(
              engine="davinci", 
              prompt=data,  # The text/question you received via WebSocket
              max_tokens=150  # You can adjust parameters as needed
            )
            answer = response.choices[0].text.strip()

            # Send back the AI's response
            await websocket.send_text(answer)
        except Exception as e:
            await websocket.send_text(str(e))
