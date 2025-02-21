from fastapi.responses import HTMLResponse
import openai
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI() 

chat_log = [{
    'role': 'system',
    'content': 'You are a Python Tutor AI,completely dedicated to helping you learn Python programming language.\
                You can ask me questions about Python, programming concepts, or any other related topics.\
                best practices and tips for writing clean, efficient code.\
                I can also help you with debugging your code and understanding error messages.\
                Please feel free to ask me anything you need help with.'
}] 
chat_responses = []
template = Jinja2Templates(directory="templates")
@app.post("/chat",response_class=HTMLResponse)
async def chat(request:Request,user_input:Annotated[str,Form()]):
   chat_log.append({'role':'user','content':user_input})
   chat_responses.append(user_input)
   response = openai.chat.completions.create(
      model="gpt-4.0-mini",
      messages=chat_log,
      temperature=0.5,
   )
   bot_response = response.choices[0].message['content']
   chat_log.append({'role':'assistant','content':bot_response})
   chat_responses.append(bot_response)

   return template.TemplateResponse("home.html",{"request":request,"chat_responses":chat_responses})