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
    font-size: 24px;
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
Engenheiro de formação, trabalhei por 4 anos em indústrias de diversos segmentos, sendo a programação de PLC e desenvolvimento de soluções IoT as minhas principais atribuições. Em 2021 comecei a trabalhar com dados (gerando, coletando, tratando e exibindo) utilizando Python como principal ferramenta. 

Trabalhar em várias fábricas, com equipamentos, máquinas e processos distintos me ajudou a desenvolver um perfil generalista e grande capacidade de resolver problemas. Também gosto bastante de aprender e integar novas tecnologias as soluções e desenvolvi um apreço particular por dados. 

Um caso interessante foi quando fui a um cliente para uma assistência técnica em uma máquina que não conhecia previamente e que o código estava em algumas linguagens diferentes (Ladder, Texto estruturado e SFC) e escrito em 4 línguas diferentes (português, inglês, alemão e italiano). Foi complicado no início, mas o problema foi resolvido. 

Um pouco da minha formação: Engenheiro Eletrônico pela Universidade Federal de Pernambuco. Bolsista do programa Ciência sem Fronteiras do Governo Federal, intercâmbio realizado no departamento de Engenharia Eletrônica da Dublin City University.""")