import os
import streamlit as st
from streamlit.web import cli as stcli

def main(environ, start_response):
    st.set_page_config(page_title="Chat with Multiple PDF", layout="wide")
    st.header("Chat with Multiple PDFs using Gemini")

    user_question = st.text_input("Ask a Question from the PDF Files")
    
    if user_question:
        user_input(user_question) # Assuming user_input is defined elsewhere

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", type="pdf", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs) # Assuming get_pdf_text is defined
                    text_chunks = get_text_chunks(raw_text) # Assuming get_text_chunks is defined
                    get_vector_store(text_chunks) # Assuming get_vector_store is defined
                    st.success("Done")
            else:
                st.warning("Please upload at least one PDF file.")
      start_response('200 OK', [('Content-Type', 'text/plain')])
      return [b'Hello World']        

# Run the Streamlit app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8501))
    stcli.main_run(
        args=["streamlit", "run", "app.py", "--server.port", str(port)],
    )
