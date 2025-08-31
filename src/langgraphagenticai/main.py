import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():    
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_streamlit_ui()
    
    if not user_controls:
        st.error("Failed to load user controls.")
        return None
    
    user_message = st.chat_input("Enter your message :")
    
    ##return user_controls