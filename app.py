import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

#Langsmit Tracking

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["langchain_tracing_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A CHAT BOT WITH OPENAI"


#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, Please answer the user user queries"),
        ("user","Question:{question}")
    ]
)


# Temperature is used to not repeat answers 
# 0 - answers will be repeated, if asked the same questions
# 1- answers will be varied each time the same question is asked
def generate_response(question, api_key,llm,temperature,max_tokens): 
    openai.api_key = api_key
    llm = ChatOpenAI(model = llm,api_key = api_key,temperature = temperature,max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})
    return answer

## Title of the app

st.title("Enhanced Q & A Chatbot with OPENAI")

#sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OPENAI API KEY:", type = "password")

##Dropdown to slect the different openai model
llm = st.sidebar.selectbox("Select the model you want to work with:",["gpt-4.1-2025-04-14","gpt-4-turbo-2024-04-09","chatgpt-4o-latest"])

#Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value =0.0,max_value = 1.0, value = 0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value = 50, max_value = 300, value = 150)


## Main interface

st.write("Go ahead and ask a question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")