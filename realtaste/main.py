from langchain_core.messages import HumanMessage

from realtaste.extractor import graph

text = "我要超值三味便當，加一隻烤龍蝦。"


for chunk in graph.stream(
    input={"messages": [HumanMessage(content=text)]},
    stream_mode="values",
):
    # Extracting bento names and modifications
    response_data = chunk.get("final_response", [])
    bento_orders = [
        {"bento_name": bento.bento_name, "modify": bento.modify}
        for data in response_data
        for bento in data.bentos
    ]

    print("Bento Orders:", bento_orders)  # Print extracted orders

# Extract bento names and modifications from the final response
# final_output = graph.invoke(input={"messages": [HumanMessage(content=text)]})
# bento_orders = [
#     {"bento_name": bento.bento_name, "modify": bento.modify}
#     for data in final_output.get("final_response", [])
#     for bento in data.bentos
# ]

# print("Final Bento Orders:", bento_orders)
