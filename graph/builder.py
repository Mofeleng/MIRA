from langgraph.graph import StateGraph, START, END
from langchain.chat_models import BaseChatModel
from langgraph.checkpoint.memory import InMemorySaver

from graph.state import State

from graph.nodes.classify_intent import classify_intent_node
from graph.nodes.prompt_llm_chat import prompt_llm_chat_node
from graph.nodes.prompt_llm_code import prompt_llm_code_node
from graph.nodes.prompt_llm_rag import prompt_llm_rag_node

def build_graph(llm: BaseChatModel):
    checkpointer = InMemorySaver()

    graph_builder = StateGraph(State)

    #Nodes
    graph_builder.add_node("classifier", classify_intent_node(llm))
    graph_builder.add_node("chat_agent", prompt_llm_chat_node(llm))
    graph_builder.add_node("code_agent", prompt_llm_code_node(llm))
    graph_builder.add_node("rag_agent", prompt_llm_rag_node(llm))

    #Edges
    graph_builder.add_edge(START, "classifier")
    graph_builder.add_conditional_edges(
        "classifier",
        lambda state: state["message_intent"],
        {
            "chat": "chat_agent",
            "knowledge": "rag_agent",
            "code": "code_agent"
        }
    )
    graph_builder.add_edge("chat_agent", END)
    graph_builder.add_edge("rag_agent", END)
    graph_builder.add_edge("code_agent", END)

    return graph_builder.compile(checkpointer=checkpointer)