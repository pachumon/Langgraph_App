import streamlit as st
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():    
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_streamlit_ui()
    
    if not user_controls:
        st.error("Failed to load user controls.")
        return None
    
    user_message = st.chat_input("Enter your message :")
    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_controls)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Failed to initialize the LLM model.")
                return None
            
            usecase = user_controls.get("selected_usecase")
            
            graph_builder = GraphBuilder(model)
            
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up graph: {e}")
                return None
            
        except Exception as e:
            st.error(f"Error initializing LLM: {e}")
            return None