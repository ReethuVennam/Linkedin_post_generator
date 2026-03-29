from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables for local development
load_dotenv()

def get_groq_api_key():
    """Get Groq API key from environment or Streamlit secrets"""
    # Try Streamlit secrets first (for deployment)
    try:
        return st.secrets["GROQ_API_KEY"]
    except (KeyError, AttributeError):
        # Fall back to environment variable (for local development)
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Please set it in environment variables or Streamlit secrets.")
        return api_key

# Initialize LLM with API key
llm = ChatGroq(groq_api_key=get_groq_api_key(), model_name="llama-3.3-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are ")
    print(response.content)





