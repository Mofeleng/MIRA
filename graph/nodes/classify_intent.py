
from langchain.chat_models import BaseChatModel
from langchain.messages import SystemMessage, HumanMessage

from graph.state import State
from schemas.intent_classifier import IntentClassifier

def classify_intent_node(llm: BaseChatModel):
    def classify_intent(state: State):
        structured_llm = llm.with_structured_output(IntentClassifier)

        result = structured_llm.invoke([
        SystemMessage("Determine / Classify whether the user wants to chat ('chat'), retrieve content ('knowledge') or change code ('code')"),
        HumanMessage(state["messages"][-1].content)
        ])

        return { "message_intent": result.message_intent }
    
    return classify_intent