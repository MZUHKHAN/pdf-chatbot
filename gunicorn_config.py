import os
from streamlit.web import cli as stcli
from app import streamlit_app  # Import the streamlit_app function from app.py

def main():
    """
    WSGI entry point for the Streamlit app.
    """
    streamlit_app()  # Call the streamlit_app function to start the Streamlit app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8501))
    stcli.main_run(
        args=[
            "streamlit",
            "run",
            os.path.basename(__file__),
            "--server.port",
            str(port),
        ],
    )
