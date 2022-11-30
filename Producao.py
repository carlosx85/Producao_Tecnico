import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
 

 

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(
    page_title="Telefonia Pública - App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
     
)


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



# ---- SIDEBAR ----
st.sidebar.header("Escolha uma opção:")

tipo = st.sidebar.multiselect(
    "Selecione um Tipo de serviço:",
    options=df["Tipo"].unique(),
    default=df["Tipo"].unique()
 )

supervisor = st.sidebar.multiselect(
    "Selecione um Supervisor:",
    options=df["Supervisor"].unique(),
    default=df["Supervisor"].unique()
)


df_selection = df.query(
    "Supervisor == @supervisor & Tipo ==@tipo"
)


# TOP KPI's

producao = df[df['Tipo'] == "Produtivo"].shape[0]
improdutivo = df[df['Tipo'] == "Improdutivo"].shape[0]
limpeza = df[df['Tipo'] == "Limpeza"].shape[0]
producao_total = improdutivo + producao



#---- GRAFICO PRODUCAO ---
labels = ['Produtivo','Improdutivo']
values = [improdutivo, producao]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()







#---- MAINPAGE ----
st.title(":bar_chart: Produção Mensal - Novembro 2022")
st.markdown("##")

st.container()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Produção Total")
    st.subheader(f"{producao_total:}")

with col2:
    st.subheader("Produção")
    st.subheader(f"{producao:}")

with col3:
    st.subheader("Improdutivo")
    st.subheader(f"{improdutivo:}")

with col4:
    st.subheader("Limpeza")
    st.subheader(f"{limpeza:}")

st.markdown("""---""")


labels = ['xxxxx','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

fig,ax =plt.subplots(figsize=(12,5))
ax.pie(values,labels=labels)
plt.show()




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)




 



