# Execução do Educadata

Consulte `docs/fontes_dados.md` antes de adquirir bases. `scripts/download_fontes.py` consulta as páginas oficiais do INEP e identifica arquivos tabulares publicados; os arquivos brutos ficam em `data/raw/` e não são versionados.

## Ambiente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

No Windows PowerShell, use `.venv\\Scripts\\Activate.ps1` para ativar o ambiente.

## Aquisição

```bash
python scripts/download_fontes.py
```

A aquisição efetiva deve respeitar a edição/ano desejado e as regras de uso da fonte.

## Processamento

Depois de mapear as colunas da publicação oficial para o contrato analítico:

```bash
python scripts/build_dashboard_data.py
```

Resultado esperado: `data/processed/indicadores_dashboard.csv`.

## Dashboard

```bash
streamlit run app.py
```

Sem dataset oficial processado, a interface usa dados sintéticos explicitamente marcados como demonstração.

## Reprodutibilidade

Registrar fonte, URL, data de acesso, ano de referência, versão/edição, transformações, cobertura, tratamento de ausências e validações realizadas.
