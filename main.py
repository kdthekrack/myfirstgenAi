from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import uvicorn
from llm_manager import LLMManager
# Initialize the LLMManager with the desired model type
# For Ollama, use "ollama"; for Gemini, use "gemini"; for Groq, use "groq"

app = FastAPI()
llmManager = LLMManager(model_type="groq")  # Change to "ollama" for Ollama model

# Pydantic models for request bodies
class LoginRequest(BaseModel):
    username: str
    password: str

class ChatRequest(BaseModel):
    message: str

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse('static/index.html')

@app.get("/chatbot", response_class=HTMLResponse)
async def read_chatbot():
    return FileResponse('static/chatbot.html')

@app.post("/login")
async def login(request: LoginRequest):
    # This is a simple example - in a real application, you would validate against a database
    if request.username == "admin" and request.password == "password":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/chat")
async def chat(request: ChatRequest):
    print(f"Received message: {request.message}")
    response = llmManager.chat(request.message)
    return {"response": f"{response}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
