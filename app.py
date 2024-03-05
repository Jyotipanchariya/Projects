 ## loading all the environment variables 

import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key="AIzaSyCH31TaKei-drXskX0kez_xabQ-8em75zw")
# function to load Gemini Pro Model and get responses 
model = genai.GenerativeModel("gemini-pro") 
def get_gemini_response(question):
    response = model.generate_content(question) 
    return response.text

## Initialize our streamlit app 

st.set_page_config(page_title="Weekend Queries") 
st.header("Lets Play...") 
input = st.text_input("Input = " , key = "input") 
submit = st.button("Ask your queries")
# When Submit is clicked 
if submit:
    response = get_gemini_response(input) 
    st.header("The Response is")
    st.write(response)