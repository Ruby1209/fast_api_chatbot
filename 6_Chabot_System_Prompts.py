from openai import OpenAI
from fastapi import FastAPI,Form
from typing import Annotated
from dotenv import load_dotenv
import os

load_dotenv()   # Load the .env file
api_key = os.getenv("OPEN_AI_API_SECRET_KEY")
openai = OpenAI(api_key=api_key)    # Initialize the OpenAI object
app = FastAPI()
chat_log = [{
    'role': 'system',
    'content': 'You are a Python Tutor AI,completely dedicated to helping you learn Python programming language.\
                You can ask me questions about Python, programming concepts, or any other related topics.\
                best practices and tips for writing clean, efficient code.\
                I can also help you with debugging your code and understanding error messages.\
                Please feel free to ask me anything you need help with.'
}] 

@app.post("/chat")  
async def chat(user_input: Annotated[str, Form()]):
    
    chat_log.append({"role": "user", "content": user_input})    # Append the user message to the chat log
    response = openai.chat.completions.create(
        model="gpt-4.0-mini",
        messages=chat_log,
        temperature=0.6
    )
    bot_response = response.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})    # Append the assistant's response to the chat
