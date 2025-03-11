import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langgraph.store.memory import InMemoryStore

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

in_memory_store = InMemoryStore(
    index={
        "embed": OpenAIEmbeddings(model="text-embedding-3-small"),
        "dims": 1536,
    }
)
