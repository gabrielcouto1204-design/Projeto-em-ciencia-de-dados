"""Métricas educacionais derivadas de bases já padronizadas."""

from __future__ import annotations

import pandas as pd


def rate(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    """Calcula taxa percentual, retornando NA quando o denominador é zero."""
    denominator = denominator.replace(0, pd.NA)
    return numerator.div(denominator).mul(100)


def abandonment_rate(abandoned: pd.Series, enrollment: pd.Series) -> pd.Series:
    """Calcula taxa de abandono sobre matrículas, em percentual.

    A fórmula só deve ser usada quando numerador e denominador vierem da
    mesma definição, população, período e unidade de análise.
    """
    return rate(abandoned, enrollment)
