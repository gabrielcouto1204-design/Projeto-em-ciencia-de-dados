"""Utilitários pequenos e testáveis para ingestão de dados oficiais."""

from pathlib import Path

import pandas as pd


def read_table(path: str | Path, **kwargs) -> pd.DataFrame:
    """Lê CSV ou Excel e retorna um DataFrame.

    A função não baixa dados automaticamente: a obtenção da fonte é separada
    da leitura local para preservar rastreabilidade e permitir auditoria.
    """
    file_path = Path(path)
    suffix = file_path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(file_path, **kwargs)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(file_path, **kwargs)

    raise ValueError(
        f"Formato não suportado: {suffix}. Use CSV, XLSX ou XLS."
    )


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza nomes de colunas sem alterar os valores das observações."""
    result = df.copy()
    result.columns = (
        result.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return result


def save_processed(df: pd.DataFrame, path: str | Path) -> None:
    """Salva uma tabela processada em CSV, criando a pasta se necessário."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)
