from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import agent_app
from langchain_core.messages = import HumanMessage.SystemMessage
from langchain_core.runnables import RunnableConfig

app = FastAPI(
    title = "RAG AI Agent API"
    description = "My Industry Level PDF Chatbot"
    version = "1.0.0"
) 
class UserRequest(BaseModel):
    query: str
    thread_id: str = "user_thread"
class AgentResponse(BaseModel):
    response: str
    thread_id: str 
    tool_used: bool

@app.post("/chat", response_model=AgentResponse)
async def chat(request: UserRequest):
    try: 
        systemMsg = SystemM