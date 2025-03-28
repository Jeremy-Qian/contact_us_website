import streamlit as st

st.title('Contact Us')

st.write('Contact Us with the following information:(Answer the question to get the emails)')
if st.text_input('Who invented see you?  *Answe is all lowercase*') == st.secrets.get('answer'):

    st.write('E-mail 1: 917592095@qq.com (Jeremy)')
    st.write('E-mail 2: joshuabatluck@gmail.com (Joshua)')

st.markdown('[Go Back](https://ramper.streamlit.app)')