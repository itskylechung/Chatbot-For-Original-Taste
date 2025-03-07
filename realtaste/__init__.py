import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = init_chat_model("gpt-4o-mini", model_provider="openai")
