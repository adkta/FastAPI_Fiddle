from fastapi import FastAPI
import uvicorn
from data_model import Custom_Prompt

app = FastAPI()

@app.post("/predict")
def get_response(custom_prompt: Custom_Prompt) -> dict[str, str]:
    return {
      "response": f"Returning the same response: {custom_prompt.prompt}"
    }

uvicorn.run(app)