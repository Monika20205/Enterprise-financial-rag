from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embeddings
from config import VECTOR_DB_PATH
import logging

logger = logging.getLogger(__name__)

def create_vector_store(chunks):
    if not chunks:
        logger.error("Error: No chunks provided to create vector store")
        raise ValueError("Cannot create vector store with empty chunks list")
    
    logger.info(f"Creating vector store with {len(chunks)} chunks")
    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(VECTOR_DB_PATH)
    logger.info(f"Vector store saved to {VECTOR_DB_PATH}")

def load_vector_store():
    embeddings = get_embeddings()
    vector_store = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store