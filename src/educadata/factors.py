from __future__ import annotations

import pandas as pd


def association_table(df: pd.DataFrame, target: str = "taxa_abandono") -> pd.DataFrame:
    """Return Pearson correlations for numeric variables, without implying causality."""
    numeric = df.select_dtypes(include="number")
    if target not in numeric:
        raise ValueError(f"Variável-alvo ausente: {target}")
    corr = numeric.corr(numeric_only=True)[target].drop(target).sort_values(key=abs, ascending=False)
    return corr.rename("correlacao").to_frame()
