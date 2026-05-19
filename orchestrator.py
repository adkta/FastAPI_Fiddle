import subprocess
import time
import nest_asyncio
from importlib_resources import files

BACKEND_PATH = files("FastAPI_Fiddle").joinpath("backend.py").as_posix()
FRONTEND_PATH = files("FastAPI_Fiddle").joinpath("frontend.py").as_posix()
# Apply async patch for Colab environments
nest_asyncio.apply()

print("🚀 Launching Backend Module...")
backend_process = subprocess.Popen(["python", BACKEND_PATH])

# Give the heavy AI model a few seconds to load up before booting the UI
time.sleep(10) 

print("🎨 Launching Frontend Module...")
frontend_process = subprocess.Popen(["python", FRONTEND_PATH])

print("\n✨ Both modules are initializing in the background.")
print("👇 Watch the logs below for your public Gradio URL Link:")