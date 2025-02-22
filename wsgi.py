import os
import streamlit as st
from streamlit.web import cli as stcli

st.set_option('server.headless', True)  # Set to True for deployment
st.set_option('runner.installTracer', False)  # Disable tracer installation

if __name__ == "__main__":
    main()
    
application = main
