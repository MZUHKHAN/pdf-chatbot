import os
from streamlit.web import cli as stcli
from app import streamlit_app  # Import the streamlit_app function from app.py

def main(environ, start_response):  # Add environ and start_response arguments
    """
    WSGI entry point for the Streamlit app.
    """
    # start_response('200 OK', [('Content-Type', 'text/html')])
    # return [b'Hello World']  # Streamlit handles rendering; no need to return "Hello World"
    streamlit_app()  # Call the streamlit_app function to start the Streamlit app

    start_response('200 OK', [('Content-Type', 'text/html')])  # or whatever you want to return
    #return [b'Hello World']

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
