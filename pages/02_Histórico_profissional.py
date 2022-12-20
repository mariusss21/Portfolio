import streamlit as st


st.set_page_config(
    page_title="Histórico profissional",
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

.css-1yy6isu p {
    word-break: break-word;
    font-size: 24px;
}

div.streamlit-expanderHeader{
    width: 100%;
    font-size: 30px;
}
</style>""", unsafe_allow_html=True)

st.markdown("# Histórico profissional")

info, skills = st.columns([7,3])

info.markdown("""
## Engenheiro de controle e automação - Ambev
#### de abril de 2021 até setembro de 2022

Era responsável por todo o ciclo de desenvolvimento de soluções, participando de reuniões para entender o problema e definir o escopo do projeto. Então passava para a execução do projeto, entrega, melhorias e manutenção. Colaborava com os projetos de outros membros da equipe

* Desenvolvimento de aplicações para otimizar os processos com Python e deploy das aplicações na plataforma Streamlit.io ou em containers (Docker).
* Desenvolvimento de dashboards (Streamlit e Grafana)
* ETL com Python e Node-Red

""")

skills.markdown("""
### Skills:
* Python (Pandas, Plotly, Streamlit)
* Bancos de dados (MySQL, Firebase, InfluxDB)
* Node-Red (Javascript)
""")

with st.expander('Principais projetos na Ambev'):
    st.write('projetos')