from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

from realtaste import llm
from realtaste.schema import BentoConfig


# Inherit 'messages' key from MessagesState, which is a list of chat messages
class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: BentoConfig


workflow = StateGraph(state_schema=AgentState)


# Define the function that calls the model
def call_model(state: AgentState):

    system_prompt = (
        "You are an expert in structured data extraction. "
        "Extract only relevant information from user input.  "
        "If an attribute's value cannot be determined, return null for that attribute.  "
        "Do not infer or assume missing details."
    )
    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    model_with_structured_output = llm.with_structured_output(BentoConfig)
    response = model_with_structured_output.invoke(messages)

    # We return a list, because this will get added to the existing list
    return {"final_response": [response]}


# Define the node and edge
workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

# Add simple in-memory checkpointer
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

text = "請來一個日式蒲燒鰻魚便當，飯多一點，醬汁少一點。"

result = app.invoke(
    input={"messages": [HumanMessage(content=text)]},
    config={"configurable": {"thread_id": "1"}},
)
print(result)
