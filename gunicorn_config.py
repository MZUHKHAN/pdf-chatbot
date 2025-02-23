import os
from streamlit.web import cli as stcli
from app import streamlit_app  # Import the streamlit_app function from app.py

def main(environ, start_response):
   
    # Call the streamlit_app function to start the Streamlit app
    streamlit_app()
   
    start_response('200 OK', [('Content-Type', 'text/html')])
    # start_response('200 OK', [('Content-Type', 'text/plain')]) # this was the original line for reference.
    return [b'Hello World']  # Streamlit handles rendering; no need to return "Hello World"

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
