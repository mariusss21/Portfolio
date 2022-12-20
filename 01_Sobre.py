import streamlit as st

st.set_page_config(
    page_title="Porfólio Mario Carvalho",
	layout="wide",
    initial_sidebar_state="expanded",
)

m = st.markdown("""
<style>
div.stButton > button:first-child{
    width: 100%;
    font-size: 18px;
}

label.css-qrbaxs{
    font-size: 18px;
}

p{
    font-size: 20px;
}

h1{
    text-align: center;
}

div.block-container{
    padding-top: 1rem;
}

div.streamlit-expanderHeader{
    width: 100%;
    font-size: 18px;
}
</style>""", unsafe_allow_html=True) #    font-weight: bold;

# Página sobre
st.markdown("# Sobre")

st.markdown("""
## Quem sou eu?
Olá, sou Mario Carvalho. Sejam bem vindos ao meu portfólio. Nasci em Natal-RN e moro em Recife-PE desde 1997 com passagens por Dublin e Sete Lagoas-MG. Sou apaixonado por resolver problemas, esportes (em especial o futebol) e livros de fantasia.

## Onde comecei?
Desde pequeno gostava muito de matemática e já tinha me decidido pela engenharia. Entrei em engenharia eletrônica e me encontrei na automação industrial. Como engenheiro (de 2016 até 2020), trabalhei em indústrias de diversos segmentos, sendo a programação de PLC e desenvolvimento de soluções IoT as minhas principais atribuições.

## O que mudou?
Python e os dados entraram no meu caminho. Ainda no meu primeiro emprego surgiram demandas que me fizeram entrar em contato com python e depois os dados (2019). Resolvi então mudar minha trajetória profissional e em 2021 surgiu a oportunidade na Ambev para testar esse novo caminho.

## Onde estou?
Saí da Ambev em setembro de 2021 e direcionei meus estudos para a **engenharia de dados**. Hoje estou cursando um bootcamp de engenharia de dados na How e um nanodegree de Data engineering na Udacity

""")