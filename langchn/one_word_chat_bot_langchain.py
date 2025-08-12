from openai import OpenAI
from dotenv import load_dotenv

import os
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def one_word_response(conversations):
    system_instruction = (
        "You are a chatbot that always responds with only one word. "
        "No matter what the user says, respond in just a single, relevant word."
    )

    all_messages = [
            {"role": "system", "content": system_instruction}
    ]

    all_messages.extend(conversations)
    print(all_messages)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= all_messages,
        temperature=0.2,
        max_tokens=1000
    )

    return response.choices[0].message.content.strip()

def main():
    print("Welcome to One-Word Bot! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break
        try:
            reply = one_word_response(user_input)
            print("Bot:", reply)
        except Exception as e:
            print("Error:", str(e))
