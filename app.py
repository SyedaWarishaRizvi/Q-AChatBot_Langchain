# conversational q%a chatbot 

import streamlit as st # session management - remember the content of each session
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

## Streamlit UI (basics)
st.set_page_config(page_title="Conversational Q&A Chatbot") # basic information for intro page
st.header("Hey, Let's Chat") # a message

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPEN_API_KEY"]=""
chat = ChatOpenAI(openai_api_key=os.environ["OPEN_API_KEY"],temperature=0.5) # initialize

# checking if key is available or not
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[SystemMessage(content="Yor are a comedian AI assistant")]

# Function to load OpenAI model and get respones
# you need to store all the schema in sessions 
# human message is from us 
# system message is how you want the chatbot to behave 
# ai message is the reply you receive from the chatbot

def get_chatmodel_response(question): # question we get from user
    # flow message is my own key
    # append the question which is the human message 
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    # append this answer to the ai message - response from the LLM model
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
# call the model
response=get_chatmodel_response(input)
submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)