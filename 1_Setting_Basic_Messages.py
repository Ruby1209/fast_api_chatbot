from openai import OpenAI

openai = OpenAI(api_key="sk-1234567890abcdef1234567890abcdef")
response = openai.chat.completions.create(
    model="gpt-4.0-mini",
    messages=[{
        'role': 'system',
        'content': 'You are a helpful assistant'
    },
    {
        'role': 'user',
        'content': 'Who won the NBA championship in 2005?'
    }]
)
print(response)
print(response.choices[0].message.content)
