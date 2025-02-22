import os
import streamlit as st
from streamlit.web import cli as stcli
import importlib
import sys

# Get the directory containing wsgi.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the current directory to Python's import search path
sys.path.insert(0, current_dir)

def main():
    #st.set_option('server.headless', True)
    #st.set_option('runner.installTracer', False)
    #logging.basicConfig(level=logging.INFO)
    #logger = logging.getLogger(__name__)

    port = int(os.environ.get("PORT", 8501))
    stcli.main_run(argv=["streamlit", "run", "app.py", "--server.port", str(port)])

    st.set_page_config(page_title="Chat with Multiple PDF", layout="wide")
    st.header("Chat with Multiple PDFs using Gemini")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", type="pdf", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Done")
            else:
                st.warning("Please upload at least one PDF file.")


if __name__ == "__main__":  # This ensures main is only called when the script is run directly
    main()
