import os
import streamlit as st
from langchain_openai import ChatOpenAI

# Load API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)