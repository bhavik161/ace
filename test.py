import streamlit as st

# Simulate chatbot request/response
user_input = st.text_input("Ask me something:")

if user_input:
    # Your chatbot processing here
    response = f"Response to: {user_input}"  # replace with your real logic
    st.write(response)

    # Initialize state
    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = None

    # Handlers to update state
    def click_yes():
        st.session_state.button_clicked = "yes"

    def click_no():
        st.session_state.button_clicked = "no"

    # Show buttons only if nothing was clicked yet
    if st.session_state.button_clicked is None:
        st.write("Do you want to do additional processing?")
        col1, col2 = st.columns(2)
        with col1:
            st.button("Yes", on_click=click_yes)
        with col2:
            st.button("No", on_click=click_no)

    # Logic after button click
    elif st.session_state.button_clicked == "yes":
        st.write("Doing additional processing...")
        # Your extra logic here
    elif st.session_state.button_clicked == "no":
        st.write("Okay, ending here.")
