import os
from streamlit.web import cli as stcli

def main(environ, start_response):
    """WSGI entry point for the Streamlit app."""
    # Ensure the path to the main Streamlit script (app.py) is correct
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")

    # Build the arguments for stcli.main_run, using the file path above
    args = ["streamlit", "run", file_path, "--server.port", str(environ.get("PORT", 8501))]

    # Start the Streamlit server
    stcli.main_run(args)

    # Indicate that the response is ready
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'']  # Return an empty iterable to satisfy the WSGI server

if __name__ == "__main__":
    main()
