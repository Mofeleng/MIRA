
from langchain.chat_models import BaseChatModel
from langchain.messages import SystemMessage, AIMessage

from graph.state import State

def prompt_llm_chat_node(llm: BaseChatModel):
    def prompt_llm_chat(state: State):
        messages = [
            SystemMessage("You are a posh elegant chatbot that uses fancy butler like english"),
            *state["messages"]
        ]

        response = llm.invoke(messages)

        return { "messages": [AIMessage(content=response.content)]}
    
    return prompt_llm_chat