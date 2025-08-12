import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load environment variables from .env
load_dotenv()

# Initialize the LangChain ChatOpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",  # Same model you used earlier
    temperature=0.2,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# System message (prompt) for chatbot behavior
system_message = SystemMessage(content="""
You are a friendly chatbot for Athletics, a website that organizes sports events.
Your job is to assist users in enrolling in sports events.

Start by asking:
1. Which sport would you like to enroll in?
2. What is your preferred location or city?

After that, follow up with questions like:
- Age group?
- Are you registering as an individual or team?
- Preferred date or time?
- Any previous experience in this sport?

Keep responses clear and engaging. Always guide the user step-by-step through the enrollment.
""")


def get_chatbot_reply(messages):
    response = llm.invoke(messages)
    return response.content.strip()

def main():
    print(" Welcome to Athletics Sports Event Enrollment Assistant!")
    print("Type 'exit' anytime to quit.\n")


    messages = [system_message]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thanks for using Athletics. See you on the field! 🏆")
            break

        messages.append(HumanMessage(content=user_input))

        try:
            bot_reply = get_chatbot_reply(messages)
            print("Bot:", bot_reply)

            messages.append(AIMessage(content=bot_reply))

        except Exception as e:
            print(" Error:", str(e))
            break

if __name__ == "__main__":
    main()
