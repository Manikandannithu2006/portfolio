import streamlit as st

# Title of the app
st.title("My Portfolio")

# About Me section
st.header("About Me")
st.write("Hello! I'm manikandan, a python developer. This is my portfolio where you can find my projects and contact information.")

# Projects section
st.header("Projects")
st.subheader("Project 1: [Project Title]")
st.write("Description of project 1. You can include links, images, or anything else to showcase your work.")

st.markdown("[View Project](link_to_project1)")  # Replace with the actual link

st.subheader("Project 2: [Project Title]")
st.write("Description of project 2.")

st.markdown("[View Project](https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_7fuslc0ogy_e&adgrpid=1316117075550739&hvadid=82257581515009&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=143956&hvtargid=kwd-82258246341113:loc-90&hydadcr=14451_2334183&msclkid=1223997c76ea1fc4ba6cfe6083cc12eb)")  # Replace with the actual link
    
# Contact section
st.header("Contact Me")
st.write("Feel free to reach out via email: [your.email@example.com]")
