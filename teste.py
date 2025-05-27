import streamlit as st
import pandas as pd
import base64

st.write('José Maurício')

st.write("""
# Minha Primeira Aplicação
""")

st.write("""Seja muito bem vindo, fique à vontade ;)""")

file_ = open("astro-astrobot.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,)
