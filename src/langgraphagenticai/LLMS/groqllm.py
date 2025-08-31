import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input['GROQ_API_KEY']
            selected_groq_model = self.user_controls_input['selected_groq_model']
            if groq_api_key=='' or groq_api_key is None:
                st.error("Please set your Groq API key in the sidebar.")
                return None
                
            llm = ChatGroq(model=selected_groq_model, api_key=groq_api_key)
        
        except Exception as e:
            st.error(f"Error initializing Groq LLM: {e}")
            llm = None
        return llm
        