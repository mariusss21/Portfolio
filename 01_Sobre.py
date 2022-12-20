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
Engenheiro de formação, trabalhei por 4 anos em indústrias de diversos segmentos, sendo a programação de PLC e desenvolvimento de soluções IoT as minhas principais atribuições. Em 2021 comecei a trabalhar com dados (gerando, coletando, tratando e exibindo) utilizando Python como principal ferramenta. 

Trabalhar em várias fábricas, com equipamentos, máquinas e processos distintos me ajudou a desenvolver um perfil generalista e grande capacidade de resolver problemas. Também gosto bastante de aprender e integar novas tecnologias as soluções e desenvolvi um apreço particular por dados. 

## O que mudou?

""")