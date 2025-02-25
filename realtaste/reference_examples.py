from langchain_core.utils.function_calling import tool_example_to_messages

from .schema import ChooseBento, Data

examples = [
    (
        "我想要吃超值三味便當並且多主菜，飯少。",
        Data(bentos=[ChooseBento(bento_name="超值三味便當", modify="多主菜，飯少")]),
    ),
    (
        "我要經典雙味便當 - 少飯，多菜。",
        Data(bentos=[ChooseBento(bento_name="超值三味便當", modify="多主菜，飯少")]),
    ),
    (
        "經典雙味便當 - 多一點豬排，少一點米飯。",
        Data(
            bentos=[
                ChooseBento(bento_name="經典雙味便當", modify="多一點豬排，少一點米飯")
            ]
        ),
    ),
    (
        "我想要超值三味便當 - 多些燒肉，少飯。",
        Data(bentos=[ChooseBento(bento_name="超值三味便當", modify="多些燒肉，少飯")]),
    ),
    (
        "我要經典雙味便當並且加點醬汁。",
        Data(bentos=[ChooseBento(bento_name="經典雙味便當", modify="加點醬汁")]),
    ),
    (
        "我需要香炆軟肋便當 - 飯減半，多些燒肉。",
        Data(
            bentos=[ChooseBento(bento_name="香炆軟肋便當", modify="飯減半，多些燒肉")]
        ),
    ),
    (
        "我想要紅燒牛肉便當並且飯少，多牛肉。",
        Data(bentos=[ChooseBento(bento_name="紅燒牛肉便當", modify="飯少，多牛肉")]),
    ),
    (
        "我選擇韓式燒肉飯便當，燒肉多一點，飯少一點。",
        Data(
            bentos=[
                ChooseBento(bento_name="韓式燒肉飯便當", modify="燒肉多一點，飯少一點")
            ]
        ),
    ),
    (
        "我要薄鹽烤鯖魚便當，飯減少，多點配菜。",
        Data(
            bentos=[ChooseBento(bento_name="薄鹽烤鯖魚便當", modify="飯減少，多點配菜")]
        ),
    ),
    (
        "我需要蒜香烤雞腿便當，飯少，多些醬汁。",
        Data(
            bentos=[ChooseBento(bento_name="蒜香烤雞腿便當", modify="飯少，多些醬汁")]
        ),
    ),
]
messages = []

for txt, tool_call in examples:
    messages.extend(tool_example_to_messages(txt, [tool_call]))
