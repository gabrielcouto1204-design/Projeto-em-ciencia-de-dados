# Execução do Educadata

## 1. Ambiente

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. Testes

```bash
pytest -q
```

## 3. Fontes oficiais

Consulte `docs/fontes_dados.md`. A rotina `scripts/download_fontes.py` consulta as páginas oficiais do INEP e identifica arquivos tabulares publicados.

```bash
python scripts/download_fontes.py
```

Os arquivos brutos ficam em `data/raw/` e são ignorados pelo Git.

## 4. Processamento

Depois de mapear as colunas da edição oficial baixada para o contrato analítico definido no projeto:

```bash
python scripts/build_dashboard_data.py
```

O resultado esperado é `data/processed/indicadores_dashboard.csv`.

## 5. Dashboard

```bash
streamlit run app.py
```

Sem dataset oficial processado, o dashboard inicia em modo demonstração com dados sintéticos claramente identificados. Esses dados servem apenas para validar a interface e nunca devem ser usados como resultado analítico.

## 6. Reprodutibilidade

Para cada atualização, registrar: fonte, URL, data de acesso, ano de referência, versão/edição, transformação aplicada, cobertura, tratamento de ausências e validações realizadas.
