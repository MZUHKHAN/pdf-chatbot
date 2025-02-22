import os
import streamlit as st
from streamlit.web import cli as stcli

st.set_option('server.headless', True)  # Set to True for deployment
st.set_option('runner.installTracer', False)  # Disable tracer installation

def main():
    port = int(os.environ.get("PORT", 8501)) # Get port from environment or use default 8501
    stcli.main_run(argv=["streamlit", "run", "app.py", "--server.port", str(port)]) 

if __name__ == "__main__":
    main()
    
application = main
