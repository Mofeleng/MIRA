
from langchain.chat_models import BaseChatModel
from langchain.messages import SystemMessage, AIMessage

from graph.state import State

def prompt_llm_code_node(llm: BaseChatModel):
    def prompt_llm_code(state: State):
        messages = [
            SystemMessage("You are a posh elegant chatbot that uses fancy butler like english. No matter what the user says, always say 'I AM THE CODING AGENT'"),
            *state["messages"]
        ]

        response = llm.invoke(messages)

        return { "messages": [AIMessage(content=response.content)]}
    
    return prompt_llm_code