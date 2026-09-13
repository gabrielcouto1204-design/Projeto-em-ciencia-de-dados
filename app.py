"""Dashboard interativo do Educadata."""
from __future__ import annotations

import sys
from pathlib import Path

import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from src.educadata.dashboard_data import load_indicator_data  # noqa: E402

st.set_page_config(page_title="Educadata", page_icon="", layout="wide")
st.title("Educadata")
st.caption("Dashboard de Monitoramento dos Dados de Evasão Escolar no Brasil")

try:
    df = load_indicator_data()
except Exception as exc:
    st.error(f"Não foi possível carregar os dados: {exc}")
    st.stop()

is_demo = (df["status"] == "demo").all()
if is_demo:
    st.warning("Modo demonstração: os números exibidos são sintéticos e NÃO representam estatísticas oficiais. Execute o pipeline após baixar e validar as bases do INEP.")
else:
    st.success("Dados processados a partir de fonte oficial validada.")

st.sidebar.header("Filtros")
years = sorted(df["ano"].dropna().unique())
selected_years = st.sidebar.multiselect("Ano", years, default=years[-3:] if len(years) >= 3 else years)
regions = sorted(df["regiao"].dropna().unique())
selected_regions = st.sidebar.multiselect("Região", regions, default=regions)

filtered = df[df["ano"].isin(selected_years) & df["regiao"].isin(selected_regions)].copy()

latest = filtered.sort_values("ano").iloc[-1] if not filtered.empty else None
c1, c2, c3, c4 = st.columns(4)
if latest is not None:
    c1.metric("Abandono", f"{latest['taxa_abandono']:.2f}%")
    c2.metric("Aprovação", f"{latest['taxa_aprovacao']:.2f}%")
    c3.metric("Reprovação", f"{latest['taxa_reprovacao']:.2f}%")
    c4.metric("Ano selecionado", int(latest["ano"]))
else:
    st.info("Nenhum dado corresponde aos filtros selecionados.")

if not filtered.empty:
    st.subheader("Evolução da taxa de abandono")
    trend = filtered.groupby(["ano", "regiao"], as_index=False)["taxa_abandono"].mean()
    st.plotly_chart(px.line(trend, x="ano", y="taxa_abandono", color="regiao", markers=True), use_container_width=True)

    st.subheader("Comparação regional")
    comparison = filtered.groupby("regiao", as_index=False)["taxa_abandono"].mean().sort_values("taxa_abandono", ascending=False)
    st.plotly_chart(px.bar(comparison, x="regiao", y="taxa_abandono"), use_container_width=True)

    st.subheader("Dados utilizados")
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.markdown("### Interpretação responsável")
st.write("Abandono escolar, evasão e fatores associados não são sinônimos. Correlação não implica causalidade. Consulte a definição, período, cobertura e fonte antes de interpretar qualquer diferença.")
st.caption("Fonte: catálogo do projeto. Em modo demonstração, os dados são sintéticos.")
