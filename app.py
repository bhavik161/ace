# app.py
import streamlit as st
from sql_generator import generate_sql_statement
from redshift_manager import create_loan_profile

st.title("Chatbot using Streamlit")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response
    sql_statement = generate_sql_statement(user_input)
    bot_response = f"SQL Statement that will be executed: {sql_statement}"
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Display SQL statement
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    
    # Execute SQL statement and get row count
    count = create_loan_profile(sql_statement)
    bot_response = f"New table lp.new_loan_profile created with number of rows = {count}"
    
    # Display execution response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    
    # Add execution response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
