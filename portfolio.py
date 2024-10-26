import streamlit as st
from PIL import Image


st.title("My Portfolio")
st.header("Welcome to My Portfolio!")
st.write("This is a brief introduction about me.")
st.write("I am Manikandan from tirunelveli")
st.write("my hobby is to develop brochure for advertisement")
st.write("I am a beginner in programming languages.")

# Open and resize the image
img = Image.open(r"C:\Users\ACER\Downloads\BZGL4585[1].JPG")
img = img.resize((300,400))  # Adjust the size (width, height) as needed
st.image(img)

st.subheader("Skills")
skills = ["Python"]
st.write(", ".join(skills))

st.subheader("Contact Me:8148277220")
st.write("You can reach me at [my email](mailto:manikandannithu62@gmail.com).")
