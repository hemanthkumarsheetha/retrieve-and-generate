import streamlit as st
import tempfile
import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.rag.retrieve import create_embeds_for_single_pdf_file
from src.services.rag.generate import generate_a_answer

st.title("PDF Upload and Q&A")

if 'file_id' not in st.session_state:
    # For caching same files in order to not create embeddings every time
    st.session_state.file_id = None
if 'current_file_name' not in st.session_state:
    st.session_state.current_file_name = None

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    if st.session_state.current_file_name != uploaded_file.name:
        # Reset file_id for new file
        st.session_state.file_id = None
        st.session_state.current_file_name = uploaded_file.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name
        
    question = st.text_input("Ask a question about the PDF content:")
    # Create embeddings from the file
    file_path = temp_path
    try:
        if st.session_state.file_id is None:
            _, file_id = asyncio.run(create_embeds_for_single_pdf_file(file_path))
            st.session_state.file_id = file_id
        answer = None
        if question and st.session_state.file_id:
            with st.spinner("Generating answer..."):
                try:
                    answer = asyncio.run(generate_a_answer(question, st.session_state.file_id))
                    st.write("**Answer:**")
                    st.write(answer)
                except Exception as e:
                    st.error(f"Error generating answer: {str(e)}")

            
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Please upload a PDF file.")
