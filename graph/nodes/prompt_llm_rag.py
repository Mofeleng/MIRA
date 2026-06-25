
from langchain.chat_models import BaseChatModel
from langchain.messages import SystemMessage, AIMessage

from graph.state import State
from rag.vector_store import vector_store

def prompt_llm_rag_node(llm: BaseChatModel):
    def prompt_llm_rag(state: State):
        query = state["messages"][-1].content
        document = vector_store.similarity_search(query, k=3)

        context = "\n".join(f"- {doc.page_content}" for doc in document)
        messages = [
            SystemMessage(f"You are a posh elegant chatbot named Mira that uses fancy butler like english. Answer the question based on the context below. If the answer is not in it say you do not know. \n\nContext:\n{context}"),
            *state["messages"]
        ]

        response = llm.invoke(messages)

        return { "messages": [AIMessage(content=response.content)]}
    
    return prompt_llm_rag