import streamlit as st
from PIL import Image

# Set the page config
st.set_page_config(page_title="Image Uploader with Custom Layout", layout="wide")

# Display the app header
st.header("Image Uploader with Custom Layout")

# Create two columns, with custom styling for the upload column
upload_col, display_col = st.columns([1, 2])
with upload_col:
    st.markdown("## Upload Image")
    # Use markdown to change the background color of only the upload column
    st.markdown(""" <style> .st-cb {background-color: grey;} </style> """, unsafe_allow_html=True)
    file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if file is not None:
    with display_col:
        st.markdown("## Uploaded Image")
        image = Image.open(file)
        st.image(image, caption='Nice image!', use_column_width=True)
        st.markdown("**Nice image!**")
else:
    with display_col:
        st.write("The uploaded image will be displayed here.")
