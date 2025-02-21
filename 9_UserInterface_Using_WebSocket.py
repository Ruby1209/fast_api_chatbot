from openai import OpenAI
from fastapi import FastAPI, Form, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
from dotenv import load_dotenv

load_dotenv()
chat_responses = []
app = FastAPI()
openai = OpenAI(api_key = os.getenv('OPENAI_API_SECRET_KEY'))
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)  # 1
async def chat_page(request: Request):  # 2
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})  # 3 

chat_log = [{'role': 'system', 'content': 'You tell jokes.'}]  # 4

@app.websocket("/ws")  # 5
async def chat(websocket: WebSocket):  # 6

    await websocket.accept()  # 7

    while True:  # 8
        user_input = await websocket.receive_text()  # 9
        chat_log.append({'role': 'user', 'content': user_input})  # 10
        chat_responses.append(user_input)  # 11

        try:  # 12
            response = openai.chat.completions.create(  # 13
                model='gpt-4.0-mini',  # 14
                messages=chat_log,  # 15
                temperature=0.6,  # 16
                stream=True  # 17
            )  # 18

            ai_response = ''  # 19

            for chunk in response:  # 20
                if chunk.choices[0].delta.content is not None:  # 21
                    ai_response += chunk.choices[0].delta.content  # 22
                    await websocket.send_text(chunk.choices[0].delta.content)  # 23
            chat_responses.append(ai_response)  # 24

        except Exception as e:  # 25
            await websocket.send_text(f'Error: {str(e)}')  # 26
            break  # 27
@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):

    chat_log.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = openai.chat.completions.create(
        model='gpt-4.0-mini',
        messages=chat_log,
        temperature=0.6
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)

    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})