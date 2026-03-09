from langchain_openai import ChatOpenAI
import streamlit as st
# from dotenv import load_dotenv


# load_dotenv()

llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    api_key=st.secrets["OPENAI_API_KEY"]
)