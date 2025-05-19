import streamlit as st
import random
from PIL import Image, ImageDraw
import os

st.set_page_config(
    page_title="Random Image Generator",  
    page_icon="🎨",                     
    layout="centered",                       
)

# Function to generate a random image
def generate_random_image():
    width, height = 300, 300  # Image dimensions
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Add random rectangles
    for _ in range(5):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        x1, x2 = sorted([x1, x2])  # Ensure valid rectangle dimensions
        y1, y2 = sorted([y1, y2])
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.rectangle([x1, y1, x2, y2], fill=color)

    # Add random circles
    for _ in range(5):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        r = random.randint(20, 50)  # Random radius
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.ellipse([x1, y1, x1 + r, y1 + r], fill=color)

    return image

# Create gallery folder if it doesn't exist
def create_gallery_folder():
    folder_name = "gallery"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

# Streamlit app
st.title("Random Image Generator")
st.write("Click the button below to generate and save a random image!")

if st.button("Generate and Save Image"):
    # Generate the random image
    img = generate_random_image()

    # Save the image in the gallery folder
    folder = create_gallery_folder()
    img_name = f"image_{random.randint(1000, 9999)}.png"  # Random file name
    img_path = os.path.join(folder, img_name)
    img.save(img_path)

    # Show the image in the app
    st.image(img, caption=f"Image saved as {img_name}")
    st.success(f"Image successfully saved in the gallery folder as {img_name}!")