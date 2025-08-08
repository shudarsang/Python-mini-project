from athletics_chat_bot_openai import get_chatbot_reply
from one_word_chat_bot_openai import one_word_response
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv
load_dotenv()
# Load API Key from .env
# FastAPI app
app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Athletics Chatbot API</title>
        </head>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
            <h1>🏆 Athletics Chatbot API</h1>
            <p>This is the backend service for the Athletics sports enrollment assistant.</p>
            <p>To use the chatbot, send a POST request to <code>/chat</code> with a list of messages.</p>
            <p>Built with ❤️ using FastAPI + OpenAI</p>
        </body>
    </html>
    """
@app.get(path="/route")
def tray():
    return "trail"


class UserMessage(BaseModel):
    messages: list  # [{"role": "user", "content": "..."}]

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat/ath", response_model=ChatResponse)
async def athlitics_ai(request: UserMessage):
    print(request.messages[-1])
    print(type(request.messages[-1]))
    try:
        reply = get_chatbot_reply(request.messages[-1])
        return {"reply": reply}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}


@app.post("/chat/one-word", response_model=ChatResponse)
async def oneword_ai(request: UserMessage):
    try:
        reply = one_word_response(request.messages)
        return {"reply": reply}
    except Exception as e:
        print(request)
        return {"reply": f"Error: {str(e)}"}