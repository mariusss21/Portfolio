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
    font-size: 26px;
}

div.streamlit-expanderHeader{
    width: 100%;
}
</style>""", unsafe_allow_html=True)

st.markdown("# Histórico profissional")

info, skills = st.columns([7,3])

info.markdown("""
## Engenheiro de controle e automação - Ambev :beer:
#### *de abril de 2021 até setembro de 2022*

Era responsável por todo o ciclo de desenvolvimento de soluções, participando de reuniões para entender o problema e definir o escopo do projeto. Então passava para a execução do projeto, entrega, melhorias e manutenção. Também colaborava com os projetos de outros membros da equipe.

* Desenvolvimento de aplicações para otimizar os processos com Python e deploy das aplicações na plataforma Streamlit.io ou em containers (Docker).
* Desenvolvimento de dashboards (Streamlit e Grafana)
* ETL com Python e Node-Red

""")

skills.markdown("""
### Skills:
* Python (Pandas, Plotly, Streamlit)
* Bancos de dados (MySQL, Firebase, InfluxDB)
* Node-Red (Javascript)
* ETL
* Grafana
* Docker
* PLC 
""")

with st.expander('Principais projetos na Ambev'):
    st.markdown("""
    ### Dashboard logística interna da fábrica:
    Projeto visava auxiliar a reposição de insumos e retirada de produto finalizado. Essa solução reduziu a zero o tempo de parada por questões logísticas resultando em uma economia estimada superior a R$ 500.000,00/mês. 
    * Ferramentas utilizadas: Node-Red para coleta de dados dos equipamentos, InfluxDB para armazenamento e dashboard no Grafana

    ### Central de alarmes da Control Tower: 
    Todos os alarmes da planta foram concentrados em uma única aplicação, o que permiteu ao operador identificar rapidamente quais máquinas estão em falha ou se houve falha em inspeções de qualidade. 
    * Ferramentas utilizadas: Node-Red para coleta de dados dos equipamentos e de arquivos CSV, armazenamento em banco MySQL e a interface desenvolvida em Python (Pandas e Streamlit).
    """)