from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI,Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
chat_log = []   # Create an empty list to store the chat log

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": "request"})