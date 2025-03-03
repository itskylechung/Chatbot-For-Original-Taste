import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from realtaste.reference_examples import messages
from .schema import Data

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    api_key=OPENAI_API_KEY,
)


prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "If you do not know the value of an attribute asked to extract, "
            "return null for the attribute's value.",
        ),
        MessagesPlaceholder("examples"),
        ("human", "{text}"),
    ]
)
structured_llm = llm.with_structured_output(schema=Data)

prompt = prompt_template.invoke(
    {
        "examples": messages,
        "text": "我想要吃超值三味便當，少飯，多菜",
    }
)
bentos_msg = structured_llm.invoke(prompt)
print(bentos_msg)
