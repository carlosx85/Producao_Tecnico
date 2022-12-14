import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import matplotlib
import seaborn as sns




# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(
    page_title="xxxTelefonia Pública - App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
     
    )   

    

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)





def get_data_from_excel():
# ---- READ EXCEL ----
    df = pd.read_excel(
    io="http://servicotp.com.br/icatel/producao/producao.xlsx",
    engine="openpyxl",
    sheet_name="Analitico",
    skiprows=0,
    usecols="A:V",
    nrows=50000,
    )
    return df

df = get_data_from_excel()


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

  
#----MENU SUPERIOR ----
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #8B008B;">
  <a class="navbar-brand" href="http://servicotp.com.br/icatel/" target="_blank">Icatel Serviços</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="http://servicotp.com.br/icatel/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://servicotp.com.br/icatel/" target="_blank">Geral</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://servicotp.com.br/icatel/" target="_blank">Técnicos</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#---- MAINPAGE ----
st.title(":bar_chart: Produção Mensal - Dezembro 2022")
st.markdown('''Análise Geral de produção dos Técnicos com relação a Telefonia de Uso Público.''')




