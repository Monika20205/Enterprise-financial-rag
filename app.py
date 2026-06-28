import streamlit as st
import os

from rag import ask_question

st.set_page_config(
    page_title="Enterprise Financial Intelligence Assistant",
    layout="wide"
)

st.title("📊 Enterprise Financial Intelligence Assistant")
st.write("Upload enterprise PDF documents and ask questions using RAG.")

if "history" not in st.session_state:
    st.session_state.history = []

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    os.makedirs("data", exist_ok=True)

    for file in uploaded_files:
        with open(os.path.join("data", file.name), "wb") as f:
            f.write(file.read())

    st.success("PDFs uploaded successfully.")
    st.info("Now run: python ingest.py")

question = st.text_input("Ask a question")

if st.button("Submit"):
    if question:
        answer, docs = ask_question(question)

        st.session_state.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Source Citations")

        for i, doc in enumerate(docs, 1):
            st.write(f"Source {i}")
            st.write(doc.metadata)

st.subheader("Conversation History")

for chat in st.session_state.history:
    st.markdown(f"**Question:** {chat['question']}")
    st.markdown(f"**Answer:** {chat['answer']}")