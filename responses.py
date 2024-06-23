import openai

openai.api_key = 'your-api-key'

def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content']

