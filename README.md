# Educadata – Dashboard de Monitoramento dos Dados de Evasão Escolar no Brasil

Projeto de Ciência de Dados para consolidar, explorar e comunicar indicadores educacionais brasileiros, com foco em abandono e evasão escolar.

## Visão geral

O **Educadata** é um dashboard interativo para monitorar abandono e evasão escolar no Brasil. A proposta integra indicadores públicos para facilitar consultas rápidas, análises comparativas e identificação de padrões relevantes para gestores educacionais, pesquisadores, órgãos públicos, jornalistas e cidadãos.

> **Princípio central:** o projeto não inventa indicadores. Cada resultado deve informar definição, população, período, cobertura e fonte oficial.

## User story

**Como** gestor educacional ou autoridade proponente de políticas públicas,  
**quero** analisar dados sobre evasão e abandono escolar no Brasil, identificando fatores associados e grupos mais vulneráveis,  
**para** compreender o problema e apoiar estratégias que aumentem a permanência e a conclusão dos estudantes.

## Critérios de aceitação

1. Apresentar dados recentes de abandono e evasão no Brasil, com evolução temporal e fontes oficiais.
2. Analisar motivos associados ao abandono, priorizando dados confiáveis, verificáveis e metodologicamente transparentes.
3. Considerar diferenças entre grupos, períodos e contextos, evitando generalizações.
4. Sinalizar ausência de dados, baixa cobertura e mudanças metodológicas.
5. Não apresentar associação como causalidade sem desenho analítico que permita inferência causal.

## Problema e justificativa

A evasão e o abandono escolar estão relacionados a desigualdades educacionais e sociais e podem reduzir oportunidades futuras. O Brasil possui grande volume de dados produzidos por instituições como INEP e IBGE, porém as informações estão distribuídas em bases, formatos e publicações diferentes.

O Educadata organiza essas informações em uma camada analítica única, com visualizações intuitivas e filtros para compreender tendências nacionais, diferenças territoriais e recortes sociodemográficos.

## Objetivos

### Geral

Construir uma solução de análise e visualização de dados capaz de apoiar o monitoramento da evasão e do abandono escolar no Brasil.

### Específicos

- Consolidar indicadores educacionais provenientes de fontes oficiais.
- Explorar a evolução temporal do abandono e da evasão.
- Comparar regiões, estados, municípios e grupos quando houver dados comparáveis.
- Investigar fatores associados ao abandono escolar.
- Incorporar aprovação, reprovação, distorção idade-série, IDEB e infraestrutura como indicadores complementares.
- Evidenciar limitações, lacunas e diferenças metodológicas.
- Disponibilizar uma interface compreensível para públicos técnicos e não técnicos.

## Público-alvo

- Gestores e profissionais da educação;
- pesquisadores, estudantes e cientistas de dados;
- órgãos públicos e formuladores de políticas;
- jornalistas e organizações da sociedade civil;
- cidadãos interessados em educação pública.

## Indicadores planejados

| Indicador | Fonte prioritária | Finalidade |
|---|---|---|
| Taxa de abandono | INEP / Censo Escolar | Monitorar abandono no sistema escolar |
| Aprovação e reprovação | INEP / Censo Escolar | Contextualizar rendimento escolar |
| Distorção idade-série | INEP | Identificar trajetórias escolares defasadas |
| IDEB | INEP | Indicador complementar de qualidade |
| Escolarização e abandono na população | IBGE / PNAD Contínua | Contextualizar o fenômeno na população |
| Infraestrutura e contexto escolar | INEP / Censo Escolar | Investigar fatores associados |

> **Importante:** abandono e evasão não são tratados automaticamente como sinônimos. O dashboard apresentará a definição e a população de referência de cada medida.

## Fontes de dados

A prioridade é utilizar fontes públicas, oficiais e documentadas:

- **INEP:** Censo Escolar, Taxas de Rendimento, Indicadores Educacionais e IDEB.
- **IBGE:** PNAD Contínua – Educação e estatísticas sociais/demográficas complementares.

O catálogo detalhado está em [`docs/fontes_dados.md`](docs/fontes_dados.md).

## Metodologia

O desenvolvimento segue um fluxo reprodutível:

1. **Entendimento:** perguntas de negócio e definições dos indicadores.
2. **Aquisição:** obtenção das bases e registro de versão/período.
3. **Preparação:** limpeza, padronização, tratamento de ausências e validação.
4. **Integração:** combinação somente por chaves compatíveis.
5. **EDA:** estatísticas descritivas, tendências, comparações e outliers.
6. **Análise de fatores:** associações entre abandono e variáveis disponíveis.
7. **Visualização:** gráficos e filtros orientados às perguntas do usuário.
8. **Validação:** conferência com as publicações e documentação oficiais.
9. **Comunicação:** interpretação, limitações e conclusões.

Mais detalhes: [`docs/metodologia.md`](docs/metodologia.md).

## Estrutura

```text
Projeto-em-ciencia-de-dados/
├── README.md
├── app.py
├── requirements.txt
├── data/
│   ├── raw/              # Bases originais; não versionar arquivos grandes
│   └── processed/        # Dados analíticos gerados pelo pipeline
├── docs/
│   ├── fontes_dados.md
│   └── metodologia.md
├── src/
│   └── educadata/        # Código reutilizável de ingestão, validação e métricas
├── tests/                 # Testes automatizados
└── dashboards/            # Componentes e documentação do dashboard
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

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
pytest -q
```

Inicie o dashboard:

```bash
streamlit run app.py
```

A interface inicial exibe apenas indicadores que estejam vinculados a dados oficiais validados. Até a ingestão das bases, valores ausentes aparecem como `—` em vez de números inventados.

## Regras de negócio e qualidade

- Priorizar dados oficiais e metodologias publicadas.
- Registrar fonte, período, definição e cobertura de cada indicador.
- Não combinar medidas incompatíveis sem explicitar a metodologia.
- Preservar a granularidade territorial e temporal sempre que possível.
- Destacar dados ausentes; não imputar valores arbitrariamente.
- Não expor dados pessoais ou confidenciais.
- Validar resultados contra as fontes originais.
- Diferenciar correlação/associação de causalidade.

## Limitações

- Algumas regiões podem ter menor disponibilidade ou qualidade de dados.
- Municípios e períodos podem apresentar lacunas.
- Mudanças metodológicas podem limitar comparações históricas.
- Indicadores agregados podem esconder diferenças importantes entre grupos.
- A disponibilidade de motivos de abandono varia conforme a pesquisa e sua metodologia.

## Estratégia de branches

- `main`: versão estável.
- `dev`: integração e validação das funcionalidades.
- `feature/*`: desenvolvimento de funcionalidades isoladas.

Fluxo:

```text
feature/* → dev → Pull Request → main
```

## Status do projeto

- [x] Estrutura inicial do repositório
- [x] Documentação do problema e metodologia
- [x] Catálogo inicial de fontes oficiais
- [x] Base de validações e testes
- [x] Esqueleto do dashboard Streamlit
- [ ] Ingestão reproduzível das bases oficiais
- [ ] Dataset analítico processado
- [ ] EDA e visualizações com dados reais
- [ ] Análise de fatores associados
- [ ] Validação final dos indicadores

## Referências oficiais

- INEP — Censo Escolar
- INEP — Indicadores Educacionais
- INEP — Taxas de Rendimento Escolar
- IBGE — PNAD Contínua

As referências e URLs de acesso estão documentadas em [`docs/fontes_dados.md`](docs/fontes_dados.md).

## Licença

A licença será definida quando a política de redistribuição de código e dados do projeto estiver consolidada. Bases oficiais não devem ser republicadas no repositório quando houver restrições de redistribuição.
