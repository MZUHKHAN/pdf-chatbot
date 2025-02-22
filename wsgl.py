import os
import streamlit as st
from streamlit.web import cli as stcli

def main():
    st.set_option('server.headless', True)
    st.set_option('runner.installTracer', False)

    port = int(os.environ.get("PORT", 8501))
    stcli.main_run(argv=["streamlit", "run", "app.py", "--server.port", str(port)])

if __name__ == "__main__":  # This ensures main is only called when the script is run directly
    main()
