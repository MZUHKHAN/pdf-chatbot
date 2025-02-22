import streamlit as st
from streamlit.web import cli as stcli

def main(*args):  
    stcli.main_run()

application = main
