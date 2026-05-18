from dotenv import load_dotenv
import os

import nest_asyncio
import uvicorn
from fastapi import FastAPI
from pyngrok import ngrok

load_dotenv()  # Loads variables from .env into os.environ

grok_auth = os.getenv("NGROK_AUTH")
print(grok_auth)


# Allow nested event loops
nest_asyncio.apply()


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Colab!"}

# Open a tunnel on port 8000
ngrok.set_auth_token(grok_auth)
public_url = ngrok.connect(8000)
print(f"Public URL: {public_url.public_url}")

# Run the server
uvicorn.run(app, port=8000)

