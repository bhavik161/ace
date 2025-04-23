import streamlit as st

# Simulate chatbot request/response
user_input = st.text_input("Ask me something:")

if user_input:
    # Your chatbot processing here
    response = f"Response to: {user_input}"  # replace with your real logic
    st.write(response)

    # Initialize state variables
    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = None

    # Show prompt only if no button was clicked yet
    if st.session_state.button_clicked is None:
        st.write("Do you want to do additional processing?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                st.session_state.button_clicked = "yes"
        with col2:
            if st.button("No"):
                st.session_state.button_clicked = "no"

    # Handle button click logic
    if st.session_state.button_clicked == "yes":
        st.write("Doing additional processing...")
        # Add your extra logic here
    elif st.session_state.button_clicked == "no":
        st.write("Okay, ending here.")
