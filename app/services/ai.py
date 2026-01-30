import os 
import json
from dotenv import load_dotenv
import requests
import base64

load_dotenv() 
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL=os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_MODEL=os.getenv("OPENROUTER_MODEL")


async def openrouter_chat(message: str, image_path:str ,role: str = "user"):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    response = requests.post(
        url=OPENROUTER_BASE_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Décris-moi cette image."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "data": image_b64 
                            }
                        }
                    ]
                }
            ]
        })
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]



