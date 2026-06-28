from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from utils.vector_store import load_vector_store
from config import GROQ_API_KEY, LLM_MODEL

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=LLM_MODEL
)

prompt = ChatPromptTemplate.from_template(
    """
You are an Enterprise Financial Intelligence Assistant.

Answer the question only using the context below.

Context:
{context}

Question:
{question}

If the answer is not available in the context, say:
"I couldn't find the answer in the uploaded documents."
"""
)

def ask_question(question):
    vector_store = load_vector_store()

    docs = vector_store.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, docs