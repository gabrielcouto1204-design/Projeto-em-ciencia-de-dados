"""Gera uma camada analítica padronizada a partir de CSVs já baixados.

A estrutura esperada pode ser adaptada em um mapeamento por fonte; este script
intencionalmente falha com mensagem clara quando as colunas oficiais não foram
mapeadas, evitando inventar indicadores.
"""
from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed" / "indicadores_dashboard.csv"
REQUIRED = {"ano", "regiao", "uf", "taxa_abandono", "taxa_aprovacao", "taxa_reprovacao"}


def main() -> None:
    files = sorted(RAW.glob("*.csv"))
    if not files:
        raise SystemExit("Nenhum CSV em data/raw. Baixe uma fonte oficial antes de gerar o dataset.")
    frames = []
    for file in files:
        df = pd.read_csv(file)
        if REQUIRED.issubset(df.columns):
            frames.append(df[list(REQUIRED)].copy())
    if not frames:
        raise SystemExit(
            "Nenhum CSV possui o contrato analítico esperado. Faça o mapeamento das colunas oficiais "
            "antes de gerar indicadores."
        )
    result = pd.concat(frames, ignore_index=True).drop_duplicates()
    result["fonte"] = "INEP — arquivo oficial processado"
    result["status"] = "oficial-processado"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUT, index=False)
    print(f"Dataset salvo em {OUT} ({len(result):,} linhas).")


if __name__ == "__main__":
    main()
