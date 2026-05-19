import gradio as gr
import httpx
import sys

async def call_fastapi_endpoint(prompt: str):
    # Route directly to the backend module port
    url = "http://127.0.0.1/predict"
    payload = {"prompt": prompt}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, timeout=30.0)
            if response.status_code == 200:
                return response.json()["response"]
            return f"Error: Status {response.status_code}"
        except Exception as e:
            return f"Cannot reach backend: {str(e)}"

# Build the UI
with gr.Blocks(title="Decoupled AI App") as demo:
    gr.Markdown("# 🤖 Decoupled UI (Gradio Frontend Module)")
    
    with gr.Row():
        input_text = gr.Textbox(label="Enter Prompt", lines=3)
        output_text = gr.Textbox(label="API Server Response", lines=5)
        
    submit_btn = gr.Button("Send to FastAPI Module", variant="primary")
    submit_btn.click(fn=call_fastapi_endpoint, inputs=input_text, outputs=output_text)

if __name__ == "__main__":
    # Launch on a different port (8080) and generate the public proxy link
    demo.launch(share=True, server_port=8080)
