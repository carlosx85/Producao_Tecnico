import pandas as pd
import streamlit as st




# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(
    page_title="Telefonia Pública - App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
     
    )   




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
        <a class="nav-link disabled" href="Producao.py">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">Geral</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="Tecnicos.py" target="_blank">Técnicos</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#---- MAINPAGE ----
st.title(":bar_chart: Produção Mensal - Dezembro 2022")
st.markdown('''Análise Geral de produção dos Técnicos com relação a Telefonia de Uso Público.''')






 



