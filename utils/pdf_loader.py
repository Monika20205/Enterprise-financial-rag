from langchain_community.document_loaders import PyPDFDirectoryLoader
from config import DATA_FOLDER
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_documents():
    try:
        loader = PyPDFDirectoryLoader(DATA_FOLDER)
        documents = loader.load()
        logger.info(f"Successfully loaded {len(documents)} documents")
        return documents
    except Exception as e:
        logger.error(f"Error loading PDF documents: {str(e)}")
        logger.info("Make sure you have valid PDF files in the data folder")
        return []