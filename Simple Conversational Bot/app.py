## Conversational Q&A Chatbot
import streamlit as st

from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_groq import ChatGroq

## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

from dotenv import load_dotenv
load_dotenv()
import os

chat=ChatGroq(model="gemma2-9b-it",temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]

## Function to load OpenAI model and get respones

def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))

    response = chat.invoke(st.session_state['flowmessages'])  # ← use .invoke()

    st.session_state['flowmessages'].append(AIMessage(content=response.content))
    return response.content


input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)

# Show full chat history
with st.expander("Chat History", expanded=True):
    for msg in st.session_state['flowmessages']:
        if isinstance(msg, HumanMessage):
            st.markdown(f"**👤 User:** {msg.content}")
        elif isinstance(msg, AIMessage):
            st.markdown(f"**🤖 Bot:** {msg.content}")
        elif isinstance(msg, SystemMessage):
            st.markdown(f"*⚙️ System Role:* {msg.content}")