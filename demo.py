import streamlit as st

if 'count' not in st.session_state:
        st.session_state['count']=0
def count_increase():
        st.session_state['count']+=1
st.button(label="click me",on_click=count_increase)
st.header(st.session_state['count'])         
x=st.slider('x')
st.write(x,'squared is',x*x)       
add_selectbox = st.sidebar.selectbox('how would you like to contacted?',('email','homephone','moblie phone'))
