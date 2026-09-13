from __future__ import annotations

from pathlib import Path

import pandas as pd


COLUMNS = ["ano", "regiao", "uf", "taxa_abandono", "taxa_aprovacao", "taxa_reprovacao", "fonte", "status"]


def load_indicator_data(path: str | Path = "data/processed/indicadores_dashboard.csv") -> pd.DataFrame:
    path = Path(path)
    if path.exists():
        df = pd.read_csv(path)
        missing = [c for c in COLUMNS if c not in df.columns]
        if missing:
            raise ValueError(f"Colunas ausentes no dataset do dashboard: {missing}")
        return df
    return demo_indicator_data()


def demo_indicator_data() -> pd.DataFrame:
    """Small synthetic dataset used only to keep the dashboard executable."""
    rows = []
    regions = {
        "Norte": ("PA", 4.8),
        "Nordeste": ("BA", 4.2),
        "Centro-Oeste": ("GO", 3.0),
        "Sudeste": ("SP", 1.9),
        "Sul": ("PR", 2.1),
    }
    for year in range(2019, 2026):
        for region, (uf, base) in regions.items():
            abandonment = round(base - (year - 2019) * 0.15, 2)
            rows.append({
                "ano": year,
                "regiao": region,
                "uf": uf,
                "taxa_abandono": abandonment,
                "taxa_aprovacao": round(91 - abandonment * 0.5, 2),
                "taxa_reprovacao": round(100 - abandonment - (91 - abandonment * 0.5), 2),
                "fonte": "DEMONSTRAÇÃO SINTÉTICA — não usar para conclusões",
                "status": "demo",
            })
    return pd.DataFrame(rows, columns=COLUMNS)
