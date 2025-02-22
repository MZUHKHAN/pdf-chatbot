import streamlit as st
   from streamlit.web import cli as stcli

   def main(*args):  # Include *args to accept any arguments passed by Gunicorn
       stcli.main_run()

   application = main  # Gunicorn will look for this variable
