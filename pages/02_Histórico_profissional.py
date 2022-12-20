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

.css-184tjsw p {
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

Trabalhei na Ambev latas minas (presencial em 2021 e remoto em 2022) no time de tecnologia da fábrica. Era responsável por todo o ciclo de desenvolvimento de soluções, participando de reuniões para entender o problema e definir o escopo do projeto. Então passava para a execução do projeto, entrega, melhorias e manutenção. Também colaborava com os projetos de outros membros da equipe.

Minha missão na equipe de tecnologia era tornar os processos mais confiáveis e facilitar as atividades dos operadores.

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
    #### [Dashboard] Logística interna da fábrica:
    Projeto visava auxiliar a reposição de insumos e retirada de produto finalizado. 
    * **Resultados alcançados:** Reduziu a zero o tempo de parada por questões logísticas resultando em uma economia estimada superior a R$ 500.000,00/mês. Ficou em segundo lugar no prêmio de melhores práticas da companhia na América Latina
    * **Ferramentas utilizadas:** Node-Red para coleta de dados dos equipamentos, InfluxDB para armazenamento e dashboard no Grafana.

    #### [Aplicação] Central de alarmes da Control Tower: 
    Todos os alarmes da planta foram concentrados em uma única aplicação para auxiliar o operador a identificar rapidamente quais máquinas estão em falha ou se houve falhas em inspeções de qualidade. 
    * **Resultados alcançados:** A centralização dos alarmes possibilitou a rápida identifição de problemas gerando redução no tempo entre o problema e ação. Os gráficos também ajudaram a entender quais falhas são mais recorrentes e impactam na produção.
    * **Ferramentas utilizadas:** Node-Red para coleta de dados dos equipamentos e de arquivos CSV, armazenamento em banco MySQL e a interface desenvolvida em Python (Pandas e Streamlit).

    #### [Aplicação] Gerenciamento da calibração:
    Importa todas e trata todas as planilhas de dados de calibração que vinham do SAP. Permitia ao operador programar as calibrações e justificar os possíveis atrasos po área.
    * **Resultados alcançados:** Propiciou ao gestor a visibilidade da calibração de todos os equipamentos da fábrica. A divisão por áreas facilitou a compreensão de quais áreas poderiam gerar problemas e contorná-los antes de acontecer.
    * **Ferramentas utilizadas:** Desenvolvido com Python, Pandas e Streamlit. Obs.: A integração com o SAP ficou para uma etapa futura

    #### [Aplicação] Gerenciamento da chegada de insumos:
    Aplicação Web que permitia entrar com os dados de todas as bobinas de alumínio que chegavam na planta. Com os dados da bobina salvos, passamos a ter o histórico e o sistema gerava automaticamente as etiquetas. Também era possível utilizar a aplicação para efetuar a leitura dos QR codes das etiquetas e realizar o inventário. 
    * **Resultados alcançados:** O principal ganhofoi em tempo para o operador tendo em vista que a aplicação agilizou o processo de entrada de insumos, a confecção de etiquetas e contagem das bobinas (anteriormente feita em papel e passada para planilha)
    * **Ferramentas utilizadas:** Desenvolvido com Python e Streamlit. Deploy na nuvem do Streamlit e banco Firebase (ambas soluções gratuitas)

    #### [Aplicação] Inventário fixo:
    O inventário de ativos fixos é realizado uma vez ao ano e compreende a coleta de dados de todas as máquinas da planta. A aplicação realiza a importação e tratamento de uma base de dados (excel) pré estabelecida e filtrava itens que não precisavam ser inventariados. O iventário em si é um formulário para colocar os dados e fotos dos equipamentos. Foi construída uma pequena dashboard para acompanhar o andamento e uma seção para gerar relatórios.
    * **Resultados alcançados:** Rápida realização do inventário obrigatório, reduzindo o impacto nas demais atividades do colaborador. Organização do relatório final com todas as informações e fotos.
    * **Ferramentas utilizadas:** Desenvolvido com Python e Streamlit.

    #### [Aplicação] Rastreabilidade:
    Imperfeições nas bobinas de alumínio atrapalham a qualidade final das latas. Essa ferramenta foi desenvolvida para se ter rastreabilidade sobre quais bobinas estão rodando no momento e de quais bobinas são os paletes em estoque/acabados. Também ajudou na automatização da produção das etiquetas.
    * **Resultados alcançados:** Conferiu rastreabilidade as bobinas facilitando identificar lotes de produto com problemas. Agilizou a atividade do operador que antes tentava realizar tudo manualmente e diminuiu o risco de erros.
    * **Ferramentas utilizadas:** Desenvolvido com Python e Streamlit.

    #### [Aplicação] Visibilidade TCS:
    O TCS é um equipamento que realiza medições de peças dos equipamentos para garantir que estão na medida certa e que realizarão corretamente as transformações da lata. Existe um software que recebe esses dados, porém é de difícil navegação e não fornecia a visibilidade desejada para o dia a dia.
    Então foi desenvolvida uma aplicação que extraía essa base de dados (.mdb) e conferia visibilidade aos principais indicadores do TCS. Também foram extraídos dados de produção e falhas do InfluxDB para auxiliar o processo de tomada de decisão.
    * **Resultados alcançados:** Facilitou a troca de turno pois bastava olhar a aplicação pra saber tudo que tinha sido feito no turno passado. Os gestores tiveram visibilidade das atividades realizadas e tinham dados para comparar com a produção e as falhas
    * **Ferramentas utilizadas:** Desenvolvido com Python, Pandas e Streamlit.
    """)