# Educadata – Dashboard de Monitoramento dos Dados de Evasão Escolar no Brasil

> Projeto de Ciência de Dados para consolidar, explorar e comunicar indicadores educacionais brasileiros, com foco em abandono e evasão escolar.

## 📌 Visão geral

O **Educadata** é uma proposta de dashboard interativo voltada ao monitoramento da evasão e do abandono escolar no Brasil. O projeto integra indicadores educacionais públicos para facilitar consultas rápidas, análises comparativas e identificação de padrões relevantes para gestores educacionais, pesquisadores, órgãos públicos, jornalistas e cidadãos.

A solução parte de uma questão central: **como transformar grandes volumes de dados educacionais dispersos em informação confiável e acionável para apoiar decisões e políticas públicas?**

## 🎯 User Story

**Como** Gestores Educacionais e Autoridades Proponentes de Políticas Públicas,

**quero** analisar dados sobre Evasão e Abandono Escolar no Brasil, identificando principais fatores e grupos mais vulneráveis,

**para** compreender causas da evasão escolar e apoiar estratégias e políticas que aumentem a permanência e a conclusão dos estudantes.

## ✅ Critérios de aceitação

1. Apresentar dados recentes de abandono e evasão no Brasil, incluindo a evolução das taxas e suas respectivas fontes oficiais.
2. Analisar os principais motivos associados ao abandono escolar, priorizando dados confiáveis, verificáveis e metodologicamente transparentes.
3. Considerar variações entre grupos de estudantes, períodos e contextos, evitando generalizações e destacando diferenças estatisticamente ou substantivamente relevantes.

## 💡 Problema e justificativa

A evasão e o abandono escolar contribuem para a manutenção das desigualdades educacionais e sociais e reduzem oportunidades futuras. O Brasil possui grande quantidade de dados públicos produzidos por instituições como INEP e IBGE, mas essas informações estão distribuídas em diferentes bases, formatos e publicações.

O Educadata propõe organizar esses dados em uma camada analítica única, com visualizações intuitivas e filtros que permitam compreender tendências nacionais e diferenças regionais e sociodemográficas.

## 🎯 Objetivos

### Objetivo geral

Construir uma solução de análise e visualização de dados capaz de apoiar o monitoramento da evasão e do abandono escolar no Brasil.

### Objetivos específicos

- Consolidar indicadores educacionais provenientes de fontes oficiais.
- Explorar a evolução temporal do abandono e da evasão.
- Comparar regiões, estados, municípios e grupos de estudantes quando houver dados disponíveis e comparáveis.
- Investigar fatores associados ao abandono escolar.
- Incorporar indicadores complementares, como aprovação, reprovação, IDEB e infraestrutura escolar.
- Evidenciar limitações, lacunas e diferenças metodológicas das bases utilizadas.
- Disponibilizar uma interface que facilite a leitura dos resultados por públicos técnicos e não técnicos.

## 👥 Público-alvo

- Gestores e profissionais da educação;
- pesquisadores, estudantes e cientistas de dados;
- órgãos públicos e formuladores de políticas;
- jornalistas e organizações da sociedade civil;
- cidadãos interessados em educação pública.

## 📊 Indicadores previstos

O dashboard poderá contemplar, conforme disponibilidade e comparabilidade das bases:

- taxa de abandono/evasão escolar;
- evolução temporal dos indicadores;
- aprovação e reprovação;
- distorção idade-série;
- IDEB;
- infraestrutura das escolas;
- características das redes de ensino;
- recortes territoriais e sociodemográficos;
- motivos associados à interrupção dos estudos, quando disponíveis em fontes oficiais ou pesquisas metodologicamente adequadas.

> **Importante:** abandono, evasão e demais conceitos não devem ser tratados como sinônimos automaticamente. Cada indicador será apresentado com sua definição, período de referência e fonte.

## 🏛️ Fontes de dados

A prioridade do projeto é utilizar fontes públicas, oficiais e documentadas, especialmente:

- **INEP – Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira:** Censo Escolar, indicadores educacionais, IDEB e demais estatísticas educacionais.
- **IBGE – Instituto Brasileiro de Geografia e Estatística:** estatísticas sociais, demográficas e educacionais complementares.
- Outras fontes governamentais poderão ser incorporadas quando houver documentação, qualidade e compatibilidade suficientes.

As fontes, versões das bases, períodos e transformações aplicadas deverão ser registradas para garantir rastreabilidade e reprodutibilidade.

## 📐 Regras de negócio

1. Priorizar dados oficiais e fontes com metodologia publicada.
2. Registrar a origem e o período de cada indicador.
3. Não combinar indicadores incompatíveis sem explicitar a metodologia.
4. Preservar granularidade territorial e temporal sempre que possível.
5. Destacar ausência de dados em vez de preencher lacunas de forma arbitrária.
6. Evitar conclusões causais quando a base permitir apenas associação.
7. Respeitar dados confidenciais e não expor informações pessoais identificáveis.
8. Facilitar consultas para decisões de curto prazo e análises históricas de longo prazo.

## ⚠️ Limitações e cuidados

- Algumas regiões podem apresentar baixa disponibilidade ou qualidade de dados.
- Existem municípios e períodos com pesquisas insuficientes.
- Mudanças metodológicas entre edições das bases podem afetar comparações históricas.
- Indicadores agregados podem esconder diferenças importantes entre grupos.
- Correlação entre fatores e abandono não implica causalidade.
- Dados confidenciais não serão publicados no dashboard.

## 🔬 Metodologia de Ciência de Dados

O desenvolvimento seguirá um fluxo reprodutível:

1. **Entendimento do problema:** definição das perguntas de negócio e dos indicadores.
2. **Aquisição:** coleta das bases oficiais e documentação das versões.
3. **Preparação:** limpeza, padronização, tratamento de ausências e validação.
4. **Integração:** combinação de bases por chaves compatíveis, como território, ano e rede de ensino.
5. **Análise exploratória:** estatísticas descritivas, tendências, comparações e identificação de outliers.
6. **Análise de fatores:** investigação de associações entre abandono e variáveis disponíveis.
7. **Visualização:** construção de gráficos e indicadores interativos orientados às perguntas do público.
8. **Validação:** conferência dos resultados contra as fontes originais e testes de consistência.
9. **Comunicação:** documentação das interpretações, limitações e conclusões.

## 🗂️ Estrutura do projeto

```text
Projeto-em-ciencia-de-dados/
├── README.md
├── data/
│   ├── raw/          # Dados originais, quando sua redistribuição for permitida
│   └── processed/    # Dados tratados
├── docs/             # Documentação e metodologia
├── notebooks/        # Exploração e análises
├── src/              # Código reutilizável de ingestão, limpeza e análise
├── dashboards/       # Arquivos/componentes do dashboard
├── .gitignore
└── LICENSE
```

## 🛠️ Tecnologias sugeridas

- Python 3.11+
- pandas e NumPy para manipulação de dados
- Matplotlib/Plotly para visualização
- Jupyter para exploração e documentação analítica
- Streamlit ou ferramenta equivalente para o dashboard interativo
- Git e GitHub para versionamento e colaboração

As tecnologias podem ser ajustadas durante a implementação conforme os requisitos do produto.

## ▶️ Como executar

A estrutura inicial foi preparada para receber a implementação do pipeline. Após a definição das dependências, recomenda-se:

```bash
git clone <URL_DO_REPOSITORIO>
cd Projeto-em-ciencia-de-dados
python -m venv .venv
```

Ativação do ambiente:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux/macOS**
```bash
source .venv/bin/activate
```

Instalação das dependências, quando o arquivo for disponibilizado:

```bash
pip install -r requirements.txt
```

## 🌿 Estratégia de branches

O projeto utiliza duas branches principais:

- `main`: versão estável, destinada às entregas consolidadas.
- `dev`: desenvolvimento, integração e validação das novas funcionalidades.

Fluxo recomendado:

```text
feature/* → dev → Pull Request → main
```

Commits devem ser pequenos, descritivos e relacionados a uma alteração lógica. A branch `dev` será utilizada para desenvolvimento e integração antes da abertura de Pull Requests para `main`.

## 🧪 Qualidade e validação

Antes de promover alterações para `main`, devem ser verificadas:

- consistência dos dados;
- ausência de duplicidades indevidas;
- tratamento documentado de valores ausentes;
- compatibilidade de períodos e definições;
- coerência dos indicadores com as fontes oficiais;
- funcionamento das visualizações e filtros;
- atualização correta da documentação.

## 📈 Resultado esperado

Espera-se que o Educadata permita visualizar rapidamente **onde**, **quando** e **para quais grupos** os indicadores de abandono apresentam maior relevância, sem perder de vista as limitações dos dados.

O produto final deve transformar dados públicos dispersos em evidências compreensíveis para apoiar pesquisa, monitoramento e formulação de políticas educacionais baseadas em dados.

## 📚 Referências institucionais

- INEP — https://www.gov.br/inep/
- IBGE — https://www.ibge.gov.br/
- Censo Escolar — https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar

## 🤝 Contribuição

1. Crie ou atualize uma branch de desenvolvimento.
2. Faça alterações pequenas e documentadas.
3. Valide os resultados localmente.
4. Registre um commit com mensagem clara.
5. Envie as alterações para `dev`.
6. Abra um Pull Request de `dev` para `main` quando a entrega estiver pronta para revisão.

## 📄 Licença

A licença definitiva deve ser definida de acordo com a política de uso e redistribuição dos códigos e dados utilizados. Dados públicos continuam sujeitos às condições e licenças de suas respectivas fontes.

---

**Educadata** — dados educacionais para decisões mais informadas.
