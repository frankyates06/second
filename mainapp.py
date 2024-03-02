import streamlit as st

# Set the page config
st.set_page_config(page_title="Greet User", layout="centered")

# Display the app header
st.header("Hello Greeting App")

# Ask for the user's name
name = st.text_input("What's your name?")

# Greet the user
if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please enter your name above.")

