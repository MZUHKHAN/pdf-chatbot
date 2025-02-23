import os
from streamlit.web import cli as stcli
from app import streamlit_app  # Import the streamlit_app function from app.py

def main(environ, start_response):  # Add environ and start_response arguments
    """
    WSGI entry point for the Streamlit app.
    """

    # Get the file path to app.py
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")

    # Build the arguments for stcli.main_run
    args = ["streamlit", "run", file_path, "--server.port", str(environ.get("PORT", 8501))]

    # Start the Streamlit server
    stcli.main_run(args)

    # Indicate that the response is ready
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'']  # Return an empty iterable to satisfy the WSGI server


if __name__ == "__main__":
    main()
