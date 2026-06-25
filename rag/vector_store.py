from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_openai.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

from rag.knowledge_base import KNOWLEDGE

load_dotenv()

vector_store = InMemoryVectorStore(OpenAIEmbeddings(model='text-embedding-3-small'))
vector_store.add_documents([Document(page_content=text) for text in KNOWLEDGE])