import uuid
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

# Local imports
from graph.builder import build_graph

load_dotenv()

llm = init_chat_model("openai:gpt-4.1-mini")

graph = build_graph(llm)

config = {
    "configurable": {
        "thread_id": uuid.uuid4()
    }
}

print("Welcome to MIRA \n Type 'exit' to end your session")
print("====================================================")

while True:
    user_message = input("> ")
    if user_message == "exit":
        break

    result = graph.invoke(
        { "messages": [HumanMessage(user_message)]},
        config=config
    )

    print(f": {result["messages"][-1].content}")
