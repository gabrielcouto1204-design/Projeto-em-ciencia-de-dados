"""Template de EDA executável como script ou notebook adaptado."""
from pathlib import Path
import pandas as pd

DATA = Path("data/processed/indicadores_dashboard.csv")

def resumo(path=DATA):
    if not path.exists():
        print("Dataset oficial ainda não disponível. Execute o pipeline de dados primeiro.")
        return
    df = pd.read_csv(path)
    print(df.info())
    print("\nNulos:\n", df.isna().mean().sort_values(ascending=False).head(20))
    print("\nResumo:\n", df.describe(include="all").transpose())
    print("\nDuplicidades:", df.duplicated().sum())

if __name__ == "__main__":
    resumo()
