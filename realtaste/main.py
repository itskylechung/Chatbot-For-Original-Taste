from langchain_core.messages import HumanMessage

from realtaste.extractor import graph

text = (
    "幫我準備五個便當，兩個紅燒牛肉便當，飯少，湯汁多，三個韓式燒肉飯便當，燒肉雙倍。"
)

config = {"configurable": {"thread_id": "2"}}

for chunk in graph.stream(
    input={"messages": [HumanMessage(content=text)]},
    config=config,
    stream_mode="values",
):
    # Extracting bento names and modifications
    response_data = chunk.get("final_response", [])
    bento_orders = [
        {"bento_name": bento.bento_name, "modify": bento.modify}
        for data in response_data
        for bento in data.bentos
    ]

    for order in bento_orders:
        print(
            f"您訂購的商品為 {order['bento_name']}，而客製化的內容為 {order['modify']}。"
        )
# Print extracted orders

# Extract bento names and modifications from the final response
# final_output = graph.invoke(input={"messages": [HumanMessage(content=text)]})
# bento_orders = [
#     {"bento_name": bento.bento_name, "modify": bento.modify}
#     for data in final_output.get("final_response", [])
#     for bento in data.bentos
# ]

# print("Final Bento Orders:", bento_orders)
