from langchain_core.utils.function_calling import tool_example_to_messages

from realtaste.schema import BentoConfig, Data

# class Example(TypedDict):
#     """A representation of an example consisting of text input and expected tool calls.

#     For extraction, the tool calls are represented as instances of pydantic model.
#     """

#     input: str  # This is the example text
#     tool_calls: List[BaseModel]  # Instances of pydantic model that should be extracted


# def tool_example_to_messages(example: Example) -> List[BaseMessage]:
#     """Convert an example into a list of messages that can be fed into an LLM.

#     This code is an adapter that converts our example to a list of messages
#     that can be fed into a chat model.

#     The list of messages per example corresponds to:

#     1) HumanMessage: contains the content from which content should be extracted.
#     2) AIMessage: contains the extracted information from the model
#     3) ToolMessage: contains confirmation to the model that the model requested a tool correctly.

#     The ToolMessage is required because some of the chat models are hyper-optimized for agents
#     rather than for an extraction use case.
#     """
#     messages: List[BaseMessage] = [HumanMessage(content=example["input"])]
#     tool_calls = []
#     for tool_call in example["tool_calls"]:
#         tool_calls.append(
#             {
#                 "id": str(uuid.uuid4()),
#                 "args": tool_call.dict(),
#                 # The name of the function right now corresponds
#                 # to the name of the pydantic model
#                 # This is implicit in the API right now,
#                 # and will be improved over time.
#                 "name": tool_call.__class__.__name__,
#             },
#         )
#     messages.append(AIMessage(content="", tool_calls=tool_calls))
#     tool_outputs = example.get("tool_outputs") or [
#         "You have correctly called this tool."
#     ] * len(tool_calls)
#     for output, tool_call in zip(tool_outputs, tool_calls):
#         messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))
#     return messages


examples = [
    # ✅ Basic Orders
    (
        "我要一個蒜香烤雞腿便當，飯少，多些醬汁。",
        Data(
            bentos=[BentoConfig(bento_name="蒜香烤雞腿便當", modify="飯少，多些醬汁")]
        ),
    ),
    (
        "我要一個紅燒牛肉便當，湯汁多一點，飯少。",
        Data(
            bentos=[BentoConfig(bento_name="紅燒牛肉便當", modify="湯汁多一點，飯少")]
        ),
    ),
    # ✅ Customization Orders
    (
        "給我一個經典雙味便當，飯少，配菜多一些，謝謝。",
        Data(
            bentos=[BentoConfig(bento_name="經典雙味便當", modify="飯少，配菜多一些")]
        ),
    ),
    (
        "我要一個香炆軟肋便當，燒肉加量，飯正常。",
        Data(
            bentos=[BentoConfig(bento_name="香炆軟肋便當", modify="燒肉加量，飯正常")]
        ),
    ),
    (
        "來一個紅燒牛肉便當，牛肉多一點，飯少，請幫我醬汁分開放。",
        Data(
            bentos=[
                BentoConfig(
                    bento_name="紅燒牛肉便當", modify="牛肉多一點，飯少，醬汁分開放"
                )
            ]
        ),
    ),
    # ✅ Multi-Person Orders
    (
        "我要一個經典雙味便當，飯少，另一個超值三味便當，飯減半，多些油蔥。",
        Data(
            bentos=[
                BentoConfig(bento_name="經典雙味便當", modify="飯少"),
                BentoConfig(bento_name="超值三味便當", modify="飯減半，多些油蔥"),
            ]
        ),
    ),
    (
        "來兩個紅燒牛肉便當，一個飯少，另一個正常，湯汁多。",
        Data(
            bentos=[
                BentoConfig(bento_name="紅燒牛肉便當", modify="飯少"),
                BentoConfig(bento_name="紅燒牛肉便當", modify="飯正常，湯汁多"),
            ]
        ),
    ),
    (
        "我要一個香炆軟肋便當，飯少，多些燒肉，另一個蒜香烤雞腿便當，飯正常，醬汁多。",
        Data(
            bentos=[
                BentoConfig(bento_name="香炆軟肋便當", modify="飯少，多些燒肉"),
                BentoConfig(bento_name="蒜香烤雞腿便當", modify="飯正常，醬汁多"),
            ]
        ),
    ),
    (
        "給我三個便當，一個韓式燒肉飯便當，燒肉加量，一個紅燒牛肉便當，飯少，最後一個經典雙味便當，正常飯。",
        Data(
            bentos=[
                BentoConfig(bento_name="韓式燒肉飯便當", modify="燒肉加量"),
                BentoConfig(bento_name="紅燒牛肉便當", modify="飯少"),
                BentoConfig(bento_name="經典雙味便當", modify="飯正常"),
            ]
        ),
    ),
    (
        "我要四個便當：兩個薄鹽烤鯖魚便當，飯正常，醬少，一個超值三味便當，飯多，最後一個蒜香烤雞腿便當，去皮，飯減半。",
        Data(
            bentos=[
                BentoConfig(bento_name="薄鹽烤鯖魚便當", modify="飯正常，醬少"),
                BentoConfig(bento_name="薄鹽烤鯖魚便當", modify="飯正常，醬少"),
                BentoConfig(bento_name="超值三味便當", modify="飯多"),
                BentoConfig(bento_name="蒜香烤雞腿便當", modify="去皮，飯減半"),
            ]
        ),
    ),
    (
        "幫我準備五個便當，兩個紅燒牛肉便當，飯少，湯汁多，三個韓式燒肉飯便當，燒肉雙倍。",
        Data(
            bentos=[
                BentoConfig(bento_name="紅燒牛肉便當", modify="飯少，湯汁多"),
                BentoConfig(bento_name="紅燒牛肉便當", modify="飯少，湯汁多"),
                BentoConfig(bento_name="韓式燒肉飯便當", modify="燒肉雙倍"),
                BentoConfig(bento_name="韓式燒肉飯便當", modify="燒肉雙倍"),
                BentoConfig(bento_name="韓式燒肉飯便當", modify="燒肉雙倍"),
            ]
        ),
    ),
    # ❌ Incorrect Orders
    (
        "我要一個便當，隨便給我一個。",
        Data(bentos=[]),  # ❌ 模糊不清，無法識別品項
    ),
    (
        "幫我做一個紅燒牛肉便當，不要牛肉。",
        Data(bentos=[]),  # ❌ 無效要求，牛肉是主食
    ),
    (
        "我要超值三味便當，加一份炸雞。",
        Data(bentos=[]),  # ❌ 錯誤，菜單上沒有炸雞
    ),
    (
        "我要一個經典雙味便當，少點飯，多點雙味。",
        Data(bentos=[]),  # ❌ 錯誤，雙味是固定組合，無法額外加量
    ),
]


messages = []

for txt, tool_call in examples:
    messages.extend(tool_example_to_messages(txt, [tool_call]))
