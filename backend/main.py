
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Message(BaseModel):
    content: str

@app.post("/api/send-to-discord")
async def send_to_discord(message: Message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url or webhook_url == "YOUR_DISCORD_WEBHOOK_URL":
        return {"error": "Discord Webhook URL not configured"}
    
    data = {"content": message.content}
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        return {"message": "Message sent successfully"}
    else:
        return {"error": "Failed to send message"}
