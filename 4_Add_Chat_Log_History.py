from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()   # Load the .env file

api_key = os.getenv("OPENAI_API_SECRET_KEY")
openai = OpenAI(api_key=api_key)    # Initialize the OpenAI object   
chat_log = []   # Create an empty list to store the chat log
while True:
    user_message = input("You: ")  # Get the user input
    if user_message.lower() == "exit":
        break
    chat_log.append({"role": "user", "content": user_message})    # Append the user message to the chat log
    response = openai.chat.completions.create(
        model="gpt-4.0-mini",
        messages=chat_log,
        temperature=0.6
    )
    chat_log.append({"role": "assistant", "content": response.choices[0].message.content})    # Append the assistant's response to the chat log   
    print("Assistant:", response.choices[0].message.content)    # Print the assistant's response
    

