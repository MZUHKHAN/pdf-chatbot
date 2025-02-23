import os
from streamlit.web import cli as stcli
from app import streamlit_app  # Import the streamlit_app function from app.py

def main(environ, start_response):  # Add environ and start_response arguments
    """
    WSGI entry point for the Streamlit app.
    """
    streamlit_app()  # Call the streamlit_app function to start the Streamlit app

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'']  # Return an empty iterable to satisfy the WSGI server

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
