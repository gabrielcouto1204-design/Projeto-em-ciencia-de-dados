"""Funções simples de validação e padronização dos dados."""

from __future__ import annotations

import pandas as pd


def require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    """Garante que as colunas obrigatórias estejam presentes."""
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {', '.join(missing)}")


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza nomes de colunas para facilitar integrações entre fontes."""
    result = df.copy()
    result.columns = (
        result.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return result


def missingness_report(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna quantidade e percentual de valores ausentes por coluna."""
    report = pd.DataFrame(
        {
            "nulos": df.isna().sum(),
            "percentual_nulos": df.isna().mean().mul(100).round(2),
        }
    )
    return report.sort_values("percentual_nulos", ascending=False)
