# Educadata — Dashboard de Monitoramento dos Dados de Evasão Escolar no Brasil

Projeto de Ciência de Dados para consolidar, explorar e comunicar indicadores educacionais brasileiros, com foco em abandono e evasão escolar.

## Visão geral

O **Educadata** é um dashboard interativo para monitorar abandono e evasão escolar no Brasil. A solução integra indicadores públicos para facilitar consultas, análises comparativas e identificação de padrões relevantes para gestores educacionais, pesquisadores, órgãos públicos, jornalistas e cidadãos.

> **Princípio central:** nenhum número é tratado como evidência sem definição, população de referência, período, cobertura, fonte e validação.

## User story

**Como** gestor educacional ou autoridade proponente de políticas públicas,  
**quero** analisar dados sobre evasão e abandono escolar no Brasil, identificando fatores associados e grupos mais vulneráveis,  
**para** compreender o problema e apoiar estratégias que aumentem a permanência e a conclusão dos estudantes.

## Critérios de aceitação

1. Apresentar dados recentes de abandono e evasão no Brasil, com evolução temporal e fontes oficiais.
2. Analisar motivos/fatores associados ao abandono, priorizando dados confiáveis, verificáveis e metodologicamente transparentes.
3. Considerar diferenças entre grupos, períodos, territórios e contextos, evitando generalizações.
4. Sinalizar ausência de dados, baixa cobertura e mudanças metodológicas.
5. Não apresentar associação como causalidade sem desenho analítico apropriado.

## Fontes oficiais

O **Censo Escolar** é coordenado pelo INEP e é a principal pesquisa estatística da educação básica brasileira. A segunda etapa coleta a situação do aluno e subsidia as taxas de aprovação, reprovação e abandono.

O INEP mantém microdados do Censo Escolar até **2025** e séries históricas das Taxas de Rendimento Escolar.

O projeto prioriza:

- **INEP:** Censo Escolar, Taxas de Rendimento, Indicadores Educacionais, IDEB e demais indicadores educacionais.
- **IBGE:** PNAD Contínua — Educação e estatísticas sociais/demográficas complementares.

As fontes, definições, períodos e regras de compatibilidade estão em [`docs/fontes_dados.md`](docs/fontes_dados.md).

## Conceitos importantes

O Educadata diferencia **abandono**, **evasão**, **movimento escolar**, **rendimento**, **escolarização** e outras medidas. Nas taxas de rendimento do INEP, abandono corresponde à situação em que o aluno deixou de frequentar as aulas; aprovação e reprovação são situações distintas.

Por isso, o projeto não soma nem compara automaticamente medidas produzidas por pesquisas diferentes. Cada indicador precisa manter sua definição e população de referência.

## Indicadores

| Indicador | Fonte prioritária | Uso |
|---|---|---|
| Taxa de abandono | INEP / Censo Escolar | Monitoramento do abandono no sistema escolar |
| Aprovação e reprovação | INEP / Censo Escolar | Contextualização do rendimento |
| Distorção idade-série | INEP | Trajetórias escolares defasadas |
| IDEB | INEP | Indicador complementar de qualidade |
| Infraestrutura e contexto escolar | INEP / Censo Escolar | Contexto e fatores associados |
| Escolarização e abandono na população | IBGE / PNAD Contínua | Contextualização sociodemográfica |
| Motivos para não frequentar/abandonar | IBGE ou pesquisas adequadas | Análise de razões quando houver cobertura e comparabilidade |

## Metodologia

1. **Entendimento:** perguntas de negócio e definições.
2. **Aquisição:** obtenção das bases oficiais e registro da versão.
3. **Preparação:** limpeza, padronização e tratamento documentado de ausências.
4. **Integração:** combinação apenas por chaves e períodos compatíveis.
5. **EDA:** estatísticas descritivas, tendências, diferenças e outliers.
6. **Fatores associados:** correlações/associações e, quando justificável, modelos estatísticos documentados.
7. **Visualização:** indicadores, séries temporais, comparações territoriais e filtros.
8. **Validação:** conferência com publicações e documentação oficiais.
9. **Comunicação:** resultados, limitações, incertezas e interpretação responsável.

## Estrutura

```text
Projeto-em-ciencia-de-dados/
├── README.md
├── LICENSE
├── requirements.txt
├── app.py
├── scripts/
│   ├── download_fontes.py
│   └── build_dashboard_data.py
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── fontes_dados.md
│   ├── metodologia.md
│   └── execucao.md
├── notebooks/
│   └── 01_eda_template.py
├── src/educadata/
│   ├── config.py
│   ├── ingestion.py
│   ├── validation.py
│   ├── metrics.py
│   ├── factors.py
│   └── dashboard_data.py
├── tests/
└── .github/workflows/ci.yml
```

## Como executar

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
pytest -q
streamlit run app.py
```

### Dados

```bash
python scripts/download_fontes.py
```

A rotina consulta as páginas oficiais do INEP e identifica arquivos tabulares publicados. Os arquivos brutos permanecem fora do Git por tamanho, reprodutibilidade e regras de redistribuição.

Depois de mapear as colunas da publicação oficial para o contrato analítico:

```bash
python scripts/build_dashboard_data.py
```

Sem dataset oficial processado, o dashboard funciona em **modo demonstração**, usando dados sintéticos explicitamente marcados como `demo`. Esses valores não representam estatísticas oficiais e não podem ser usados em conclusões.

## Qualidade e governança

- Priorizar fontes oficiais e documentação metodológica.
- Registrar fonte, URL, data de acesso, edição, período e transformações.
- Não imputar valores ausentes arbitrariamente.
- Não ocultar baixa cobertura territorial.
- Validar indicadores contra a fonte original.
- Não publicar dados pessoais ou confidenciais.
- Respeitar anonimização, LGPD e regras de acesso das bases.
- Correlação/associação não implica causalidade.

## Testes e CI

O projeto possui testes automatizados para validação, ingestão e persistência. O GitHub Actions executa a suíte em pushes e Pull Requests para `dev` e `main`.

## Limitações

- Disponibilidade e qualidade podem variar por território e período.
- Mudanças metodológicas podem limitar comparações históricas.
- Indicadores agregados podem esconder desigualdades entre grupos.
- Motivos de abandono nem sempre estão disponíveis na mesma fonte ou granularidade.
- Bases públicas podem ter regras específicas de acesso, anonimização e redistribuição.

## Estratégia de branches

- `main`: versão estável.
- `dev`: integração e validação.
- `feature/*`: funcionalidades isoladas.

Fluxo:

```text
feature/* → dev → Pull Request → main
```

## Status

- [x] Estrutura do repositório
- [x] README e documentação metodológica
- [x] Catálogo de fontes oficiais
- [x] Dicionário inicial de indicadores
- [x] Camada de ingestão e validação
- [x] Testes automatizados
- [x] CI com GitHub Actions
- [x] Dashboard Streamlit funcional
- [x] Modo demonstração seguro
- [x] Rotina de descoberta das publicações oficiais
- [ ] Mapear automaticamente cada edição dos arquivos oficiais para o contrato analítico
- [ ] Gerar dataset nacional oficial processado
- [ ] EDA final com dados reais
- [ ] Integrar recortes territoriais/sociodemográficos disponíveis
- [ ] Incorporar análise sistemática dos motivos de abandono
- [ ] Validar indicadores finais contra as publicações do INEP/IBGE
- [ ] Fazer merge da PR para `main` após revisão

