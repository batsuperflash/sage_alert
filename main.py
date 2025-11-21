from fastapi import FastAPI, Request
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        await client.post(url, data={
            "chat_id": CHAT_ID,
            "text": text
        })

@app.post("/sage")
async def sage_webhook(req: Request):
    payload = await req.json()
    message = f"🔔 SAGE ALERT\n\n{payload}"
    await send_telegram_message(message)
    return {"status": "ok"}
