"""Dashboard inicial do Educadata."""

import streamlit as st

st.set_page_config(page_title="Educadata", page_icon="📊", layout="wide")

st.title("Educadata")
st.subheader("Dashboard de Monitoramento dos Dados de Evasão Escolar no Brasil")

st.info(
    "Esta versão inicial prepara a estrutura do dashboard. Os indicadores "
    "serão exibidos somente após validação da fonte, período, definição e cobertura."
)

col1, col2, col3 = st.columns(3)
col1.metric("Abandono", "—", help="Aguardando base oficial validada")
col2.metric("Evasão", "—", help="Aguardando definição e base compatíveis")
col3.metric("IDEB", "—", help="Aguardando integração da série oficial")

st.markdown("### Próximas integrações")
st.markdown(
    "- INEP: Censo Escolar e indicadores educacionais\n"
    "- IBGE: contexto territorial e sociodemográfico\n"
    "- Séries temporais e recortes por território e grupos\n"
    "- Alertas para ausência de dados e baixa cobertura"
)

st.caption("Educadata • dados oficiais, rastreabilidade e interpretação responsável")
