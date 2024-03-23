from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to load Gemini Model 
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

### Streamlit Configuration

st.set_page_config(page_title='QandA Demo')
st.header("Gemini LLM APplication")

input = st.text_input("INput " ,key='input')
submit=st.button("Ask the question")

##WHen Submit is clicked

if submit:
    response = get_gemini_response(input)
    st.write(response)    
