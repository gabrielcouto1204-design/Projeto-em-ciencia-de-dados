import pandas as pd
import pytest

from src.educadata.validation import missingness_report, normalize_column_names, require_columns


def test_normalize_column_names():
    df = pd.DataFrame({" Ano do Censo ": [2024], "Taxa de Abandono (%)": [2.5]})
    result = normalize_column_names(df)
    assert list(result.columns) == ["ano_do_censo", "taxa_de_abandono"]


def test_require_columns_raises_for_missing():
    with pytest.raises(ValueError, match="ausentes"):
        require_columns(pd.DataFrame({"ano": [2024]}), ["ano", "taxa"])


def test_missingness_report():
    result = missingness_report(pd.DataFrame({"a": [1, None], "b": [1, 2]}))
    assert result.loc["a", "nulos"] == 1
    assert result.loc["a", "percentual_nulos"] == 50.0
