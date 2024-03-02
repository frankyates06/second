import streamlit as st
from PIL import Image

# Set the page config
st.set_page_config(page_title="Simple Image Uploader", layout="centered")

# Display the app header
st.header("Simple Image Uploader")

# File uploader widget
file = st.file_uploader("Upload your image here.", type=["jpg", "jpeg", "png"])

if file is not None:
    # Display the uploaded image
    image = Image.open(file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Display the message
    st.markdown("**Nice image!**")
else:
    st.write("Upload an image to see it displayed here.")
