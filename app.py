import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import matplotlib
import seaborn as sns
from streamlit_lottie import st_lottie
import requests



st.set_page_config(
    page_title="Telefonia Pública - App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
     
    )   





with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


 
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def get_data_from_excel():
# ---- READ EXCEL ----
    df = pd.read_excel(
    io="producao.xlsx",
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
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

  
#----MENU SUPERIOR ----
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #8B008B;">
  <a class="navbar-brand" href="app.py" target="_blank">IC Serviços</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="Producao.py">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="Tecnicos.py" target="_blank">Geral</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="app.py" target="_blank">Técnicos</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)







# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
 

 

 


# TOP KPI's

producao = df[df['Tipo'] == "Produtivo"].shape[0]
improdutivo = df[df['Tipo'] == "Improdutivo"].shape[0]
limpeza = df[df['Tipo'] == "Limpeza"].shape[0]
producao_total = improdutivo + producao






# Data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')



# Row A


col1, col2 = st.columns(2)

with col1:  
    st_lottie(lottie_coding, height=300, key="coding")


with col2:
   st.header("Produção - 12/2022")
   st.metric("",f"{producao_total:}", "")  




# Row B
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Produção - Total")
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




# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df.groupby(by=["Tipo"]).count()[["RE"]] 
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="RE",
    y=sales_by_product_line.index,
    orientation="h",
    title="",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# GRAFICO DE PIZZA
labels = 'Produtivo', 'Improdutivo'
sizes = [producao, improdutivo]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=50)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# COLUNA PIZZA  + PARETO
left_column, right_column = st.columns(2)
left_column.pyplot(fig1)
right_column.plotly_chart(fig_product_sales, use_container_width=True)



# df.groupby(by=[ "Tipo", "Dia" ]).count()[["Seq"]] 
# chart_datax = pd.DataFrame(df["Dia"].unique(),3, columns=df["Tipo"].unique())
# st.area_chart(chart_datax)
 

pd.DataFrame()
chart_data = pd.DataFrame(np.random.randn(30, 3),    columns=df["Tipo"].unique())
st.line_chart(chart_data)



# LISTAGEM tipo
st.title(":bar_chart: Listagem por Tipo")
df


dx = pd.crosstab(df.Supervisor, df.Tipo , margins=True,  margins_name="Total")
st.title(":bar_chart: Produção Supervisor")
dx



# LISTAGEM DIA
st.title(":bar_chart: Listagem por Dia")
da=pd.crosstab(df.Tecnico, df.Dia , margins=True,  margins_name="Total")
da



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")








# ---- CONTACT ----
with st.container():
    st.write("Contato")
    st.write("---")
 

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/carlos.santosx85@hotmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Seu Nome" required>
        <input type="email" name="email" placeholder="Seu E-mail" required>
        <textarea name="message" placeholder="Sua Mensagem" required></textarea>
        <button type="submit">Enviar Mensagem</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()





 



