from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()   # Load the .env file

api_key = os.getenv("OPENAI_API_SECRET_KEY")
openai = OpenAI(api_key=api_key)
response = openai.chat.completions.create(
    model="gpt-4.0-mini",
    messages=[
         {
              'role': 'system',
              'content': 'You are a helpful assistant'
         },
         {
              'role': 'user',
              'content': 'Write me a 3 paragraph bio'
         }
    ],
    temperature=1.5

)
print(response.choices[0].message.content)