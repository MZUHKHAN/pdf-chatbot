# wsgi.py

import streamlit as st
from streamlit.web import cli as stcli

def main():
    stcli.main_run()

application = main  # Make the application object available to Gunicorn
