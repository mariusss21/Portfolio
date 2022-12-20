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

sobre, foto = st.columns([8,2])

sobre.markdown("""
## Quem sou eu?
Olá, sou Mario Carvalho. Sejam bem vindos ao meu portfólio. Nasci em Natal-RN e moro em Recife-PE desde 1997 com passagens por Dublin e Sete Lagoas-MG. Sou apaixonado por resolver problemas, esportes (em especial o futebol) e livros de fantasia.

## Onde comecei?
Desde pequeno gostava muito de matemática e já tinha me decidido pela engenharia. Entrei em engenharia eletrônica e me encontrei na automação industrial. Como engenheiro (de 2016 até 2020 na GC Automação), trabalhei em indústrias de diversos segmentos, sendo a programação de PLC e desenvolvimento de soluções IoT as minhas principais atribuições.

""")

foto.image('mario_carvalho.jpg')

st.markdown("""

## O que mudou?
Na GC eu tinha demandas variadas e em uma delas Python e dados entraram no meu caminho (em 2019). Após alguns cursos na área o meu interesse aumentou e resolvi então mudar minha trajetória profissional. Em 2021 consegui a oportunidade na Ambev para testar esse novo caminho, mas ainda contratado como engenheiro.

## Onde estou?
Saí da Ambev em setembro de 2021 e entrei de cabeça na **engenharia de dados**. 

**Hoje estou cursando um bootcamp de engenharia de dados na How, um nanodegree de Data engineering na Udacity e aperfeiçoando meus conhecimentos em Pyhton e SQL.'**

""")