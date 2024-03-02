import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Set the page config
st.set_page_config(page_title="Dino Detector - Simplified", layout="centered")

# Display the app header and instructions
st.image('static/dino-logo.png', width=100)
st.header("DINO DETECTOR: Simplified", divider='rainbow')
st.markdown('_Upload your image and let\'s add a fun dinosaur touch!_')

# File uploader widget
file = st.file_uploader("Upload your image here.", type=["jpg", "jpeg", "png"])

# Columns for showing the original and modified images
img, result = st.columns(2)

with img:
    st.info('Your uploaded image.', icon="ℹ️")
    if file is not None:
        image = Image.open(file)
        st.image(image, caption='Original Image', use_column_width=True)

with result:
    st.info('Your image with a dinosaur touch!', icon="ℹ️")
    if file is not None:
        # Adding a simple overlay or modification to the image
        # For demonstration, let's just add a simple text overlay as we can't actually detect dinosaurs
        modified_image = image.copy()
        draw = ImageDraw.Draw(modified_image)
        # Trying to use a default font, this might need adjustment based on your environment
        try:
            font = ImageFont.truetype("arial.ttf", size=45)
        except IOError:
            font = ImageFont.load_default()
        text = "Could be a Dinosaur here!"
        textwidth, textheight = draw.textsize(text, font)

        # Positioning the text at the bottom center
        width, height = modified_image.size
        x = (width - textwidth) / 2
        y = height - textheight - 10
        draw.text((x, y), text, font=font, fill=(255, 0, 0))

        st.image(modified_image, caption='Modified Image', use_column_width=True)

st.link_button('Feedback, Issues, or Contributions', "https://github.com/your-repo/your-project/issues", use_container_width=True)
