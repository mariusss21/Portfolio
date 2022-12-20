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
## Engenheiro de controle e automação - Ambev :beer: :bar_chart:
#### *de abril de 2021 até setembro de 2022*

Trabalhei na Ambev latas minas (presencial em 2021 e remoto em 2022) no time de tecnologia da fábrica. Era responsável por todo o ciclo de desenvolvimento de soluções, desde a definição e entendimento do problema até a entrega do produto.

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
* Programação de CLPs (Controladores Lógicos Programáveis)  
""")

with st.expander('Principais projetos na Ambev'):
    st.markdown("""
    #### [Dashboard] Logística interna da fábrica:
    O processo de reposição de insumos e produto finalizado pode gerar paradas de máquina que atrapalham a produção diária. Como não havia visibilidade para os operadores e nem pra gestão, o risco era bem alto. A dashboard foi então desenvolvida para solucionar essa falta de visibilidade. 
    * **Resultados alcançados:** Reduziu a zero o tempo de parada por questões logísticas resultando em uma economia estimada superior a R$ 500.000,00/mês. O projeto ficou em segundo lugar no prêmio de melhores práticas da companhia na América Latina
    * **Ferramentas utilizadas:** Node-Red para coleta de dados dos equipamentos, InfluxDB para armazenamento e dashboard no Grafana.

    #### [Aplicação] Central de alarmes da Control Tower: 
    A companhia possui mais de 80 máquinas em 3 linhas de produção, porém não havia nenhum lugar onde eles estivessem concentrados. Então todos os alarmes da planta foram concentrados em uma única aplicação para auxiliar o operador. 
    * **Resultados alcançados:** A centralização dos alarmes possibilitou a rápida identifição de problemas gerando redução no tempo entre o problema e ação. Os gráficos também ajudaram a entender quais falhas são mais recorrentes e impactam na produção.
    * **Ferramentas utilizadas:** Node-Red para coleta de dados dos equipamentos e de arquivos CSV, armazenamento em banco MySQL e a interface desenvolvida em Python (Pandas e Streamlit).

    #### [Aplicação] Gerenciamento da calibração:
    A calibração dos equipamentos era gerenciada em planilhas Excel parcialmente automatizadas. Utilizar o Excel gerava muita perda de informações, problemas de versionamento e edições indevidas. 
    Então foi desenvolvida uma aplicação para importar/tratar as planilhas de dados de calibração que vinham do SAP. Foram adiciondads funcionalidades de planejamento de calibração e justificativa de atrasos (questão complicada para auditorias)
    * **Resultados alcançados:** Propiciou ao gestor a visibilidade da calibração de todos os equipamentos da fábrica. A divisão por áreas facilitou a compreensão de quais áreas poderiam gerar problemas e contorná-los antes de acontecer.
    * **Ferramentas utilizadas:** Desenvolvido com Python, Pandas e Streamlit. Obs.: A integração com o SAP ficou para uma etapa futura

    #### [Aplicação] Gerenciamento da chegada de insumos:
    A chegada de insumos a planta demandava dos operadores anotar (em papel) as informações da bobina de alumínio, depois colocar as informações no Excel e posteriormente editar um Excel para montar a etiqueta. Também há o processo de contagem de bobinas que é feito manualmente.
    Foi desenvolvida uma aplicação Web que permitia entrar com os dados de todas as bobinas que chegavam na planta através de um formulário simples. Esses dados são armazenados em banco para ter histórico e são utilizados para automatização das etiquetas. Foi também adicionada uma funcionalidade para leitura de QR code das etiquetas para facilitar a contagem. 
    * **Resultados alcançados:** O principal ganho foi em tempo para o operador tendo em vista que a aplicação agilizou o processo de entrada de insumos, a confecção de etiquetas e contagem das bobinas (anteriormente feita em papel e passada para planilha)
    * **Ferramentas utilizadas:** Desenvolvido com Python e Streamlit. Deploy na nuvem do Streamlit e banco Firebase (ambas soluções gratuitas)

    #### [Aplicação] Inventário fixo:
    O inventário de ativos fixos é realizado uma vez ao ano e compreende a coleta de dados de todas as máquinas da planta. 
    A aplicação realiza a importação e tratamento de uma base de dados (Excel) pré disponibilizada pelo corporativo e filtra itens que não precisavam ser inventariados. O iventário em si é um formulário que possibilita colocar os dados e fotos dos equipamentos. Foi construída uma pequena dashboard para acompanhar o andamento e uma seção para gerar relatórios.
    * **Resultados alcançados:** Rápida realização do inventário obrigatório, reduzindo o impacto nas demais atividades do colaborador. Organização do relatório final com todas as informações e fotos.
    * **Ferramentas utilizadas:** Desenvolvido com Python e Streamlit.

    #### [Aplicação] Rastreabilidade:
    Imperfeições nas bobinas de alumínio atrapalham a qualidade final das latas. Essa ferramenta foi desenvolvida para se ter rastreabilidade sobre quais bobinas estão rodando no momento e de quais bobinas são os paletes em estoque/acabados. Também ajudou na automatização da produção das etiquetas.
    * **Resultados alcançados:** Conferiu rastreabilidade as bobinas facilitando identificar lotes de produto com problemas. Agilizou a atividade do operador que antes tentava realizar tudo manualmente e diminuiu o risco de erros.
    * **Ferramentas utilizadas:** Desenvolvido com Python e Streamlit.

    #### [Aplicação] Visibilidade TCS:
    O TCS é um equipamento que realiza medições de peças dos equipamentos para garantir que estão na medida certa e que realizarão corretamente as transformações da lata. Existe um software que recebe esses dados, porém é de difícil navegação e não fornecia a visibilidade desejada para o dia a dia.
    Então foi desenvolvida uma aplicação para extrair a base de dados do TCS (um arquivo .mdb) e conferir visibilidade aos principais indicadores do TCS. Também foram extraídos dados de produção e falhas do InfluxDB para auxiliar o processo de tomada de decisão.
    * **Resultados alcançados:** Facilitou a troca de turno pois bastava olhar a aplicação pra saber tudo que tinha sido feito no turno passado. Os gestores tiveram visibilidade das atividades realizadas e tinham dados para comparar com a produção e as falhas
    * **Ferramentas utilizadas:** Desenvolvido com Python, Pandas, Streamlit e MySQL.
    """)

info, skills = st.columns([7,3])

info.markdown("""
## Engenheiro de controle e automação - GC Automação :factory: :computer:
#### *de agosto de 2016 até dezembro de 2020*

* Desenvolvimento de projetos IoT utilizando gateway IoT2040 (Siemens) com Linux, Node-Red, Python e Arduino/ESP8266. 
* Programação de PLCs em várias linguagens (texto estruturado, Ladder e diagrama de blocos). Conversão de aplicações de CLP's em projetos de retrofit. Configuração e parametrização de inversores de frequência e soft-starters. Comissionamento e Startup de máquinas e processos industriais. 
* Serviços de assistência técnica e projetos em indústrias de diferentes segmentos (Mondelez, Campari, Ball, Bimbo, Lonza, entre outras). Elaboração de material e realização de treinamentos.
* Programação de microcontroladores (Arduino e esp8266), design e confecção de PCB e responsável pelo gerenciamento das demais atividades do setor de IoT. 
* Atuação em projetos de campo em Automação Industrial, supervisão de equipe de eletricistas, comissionamento de painéis, programação de CLPs e IHMs (Rockwell: PanelView, SLC 500, ControlLogix, CompactLogix; e Siemens: SIMATIC HMI, S7-1500, S7-1200, Logo!) e análise de diagramas elétricos. 
* Resolução de problemas relacionados a redes industriais (Modbus, Ethernet/IP, DeviceNet, Profinet e AS-Interface).

""")

skills.markdown("""
### Skills:
* Python (Pandas, Plotly, Streamlit)
* Node-Red (Javascript)
* Programação de CLPs (Controladores Lógicos Programáveis) 
* Programação de IHMs (Interface homem máquina)
* IoT (Arduino, Esp8266 e IoT2040 da Siemens)
""")

with st.expander('Principais projetos na GC Automação'):
    st.markdown(""" 


    """)