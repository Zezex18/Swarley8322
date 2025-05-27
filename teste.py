import streamlit as st
import pandas as pd
import streamlit as st
import base64


st.write('José Maurício')

st.write("""
# Minha Primeira Aplicação
""")

st.write("""Seja muito bem vindo, fique à vontade ;)""")

"""### gif from local file"""
file_ = open("file:///D:/user/C3008187/Downloads/astro-astrobot.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
