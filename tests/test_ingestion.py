import pandas as pd
import pytest

from src.educadata.ingestion import normalize_column_names, read_table, save_processed


def test_normalize_ingestion_columns():
    df = pd.DataFrame({" UF / Município ": ["SP"]})
    result = normalize_column_names(df)
    assert list(result.columns) == ["uf_municipio"]


def test_read_csv(tmp_path):
    path = tmp_path / "dados.csv"
    pd.DataFrame({"ano": [2024], "abandono": [2.5]}).to_csv(path, index=False)
    result = read_table(path)
    assert result.loc[0, "abandono"] == 2.5


def test_read_table_rejects_unknown_extension(tmp_path):
    path = tmp_path / "dados.json"
    path.write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="Formato não suportado"):
        read_table(path)


def test_save_processed_creates_parent(tmp_path):
    path = tmp_path / "processed" / "indicadores.csv"
    save_processed(pd.DataFrame({"ano": [2024]}), path)
    assert path.exists()
