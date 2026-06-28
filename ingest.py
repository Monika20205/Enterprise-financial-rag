from utils.pdf_loader import load_documents
from utils.chunker import split_documents
from utils.vector_store import create_vector_store

def main():
    print("Loading PDF documents...")
    documents = load_documents()
    
    if not documents:
        print("Error: No documents loaded. Please add PDF files to the 'data' folder.")
        return

    print(f"Successfully loaded {len(documents)} documents")
    
    print("Splitting documents into chunks...")
    chunks = split_documents(documents)
    
    if not chunks:
        print("Error: No chunks created from documents.")
        return
    
    print(f"Successfully created {len(chunks)} chunks")

    print("Creating FAISS vector database...")
    create_vector_store(chunks)

    print("Vector database created successfully!")

if __name__ == "__main__":
    main()