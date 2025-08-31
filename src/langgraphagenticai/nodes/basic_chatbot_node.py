

from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """A basic chatbot node that handles user input and generates responses."""

    def __init__(self, llm_model):
        self.llm_model = llm_model

    def process_input(self, state:State)-> dict:
        """Process user input and generate a response using the LLM model."""
        
        return {"messages": self.llm_model.invoke(state["messages"])}