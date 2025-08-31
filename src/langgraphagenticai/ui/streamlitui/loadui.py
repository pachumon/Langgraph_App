import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 "+ self.config.get_page_title(),layout="wide")
        st.header("🤖 "+ self.config.get_page_title())
        
        with st.sidebar:
            llm_options = self.config.get_llms()
            usecase_options = self.config.get_usecases()
            
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)
            
            if self.user_controls['selected_llm'] == 'Groq':
                groq_models = self.config.get_groq_models()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Groq Model", groq_models)
                self.user_controls['GROQ_API_KEY'] = st.session_state['GROQ_API_KEY'] = st.text_input("API Key", type="password")
                
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your Groq API Key in the sidebar to proceed.")
                    
            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", usecase_options)
            
        return self.user_controls
        