from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from realtaste import llm
from realtaste.reference_examples import messages
from realtaste.schema import ChooseBento, Data

# structured_llm = llm.with_structured_output(schema=ChooseBento)


prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert in structured data extraction. "
            "Extract only relevant information from user input.  "
            "If an attribute's value cannot be determined, return null for that attribute.  "
            "Do not infer or assume missing details.",
        ),
        # Please see the how-to about improving performance with
        # reference examples.
        MessagesPlaceholder("examples"),
        ("human", "{text}"),
    ]
)

runnable = prompt_template | llm.with_structured_output(
    schema=Data,
    method="function_calling",
    include_raw=False,
)
text = "我要一個香酥炸雞腿便當，飯正常，醬汁另外放。"

print(runnable.invoke({"text": text, "examples": messages}))
# prompt = prompt_template.invoke({"text": text})
# structured_llm.invoke(prompt)
