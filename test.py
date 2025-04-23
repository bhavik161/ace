import streamlit as st

# Simulate chatbot request/response
user_input = st.text_input("Ask me something:")

if user_input:
    # Your chatbot processing here
    response = f"Response to: {user_input}"  # replace with your real logic
    st.write(response)

    # Show the additional processing prompt
    st.write("Do you want to do additional processing?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            # Additional processing logic
            st.write("Doing additional processing...")
            # Your extra logic here
    with col2:
        if st.button("No"):
            st.write("Okay, ending here.")
