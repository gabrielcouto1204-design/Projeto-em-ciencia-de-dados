# Educadata – Dashboard de Monitoramento dos Dados de Evasão Escolar no Brasil

> Projeto de Ciência de Dados para consolidar, explorar e comunicar indicadores educacionais brasileiros, com foco em abandono e evasão escolar.

VISÃO GERAL: 

- O ´´Educadata´´ é uma proposta de dashboard interativo voltada ao monitoramento da evasão e do abandono escolar no Brasil. O projeto integra indicadores educacionais públicos para facilitar consultas rápidas, análises comparativas e identificação de padrões relevantes para gestores educacionais, pesquisadores, órgãos públicos, jornalistas e cidadãos.

A solução parte de uma questão central: como transformar grandes volumes de dados educacionais dispersos em informação confiável e acionável para apoiar decisões e políticas públicas?

USER STORY:

- Como --> Gestores Educacionais e Autoridades Proponentes de Políticas Públicas,

quero --> analisar dados sobre Evasão e Abandono Escolar no Brasil, identificando principais fatores e grupos mais vulneráveis,

para --> compreender causas da evasão escolar e apoiar estratégias e políticas que aumentem a permanência e a conclusão dos estudantes.

CRITÉRIOS DE ACEITAÇÃO:

1.  Apresentar dados recentes de abandono e evasão no Brasil, incluindo a evolução das taxas e suas respectivas fontes oficiais.
2.  Analisar os principais motivos associados ao abandono escolar, priorizando dados confiáveis, verificáveis e metodologicamente transparentes.
3.  Considerar variações entre grupos de estudantes, períodos e contextos, evitando generalizações e destacando diferenças estatisticamente ou substantivamente relevantes.

PROBLEMA E JUSTIFICATIVA:

A evasão e o abandono escolar contribuem para a manutenção das desigualdades educacionais e sociais e reduzem oportunidades futuras. O Brasil possui grande quantidade de dados públicos produzidos por instituições como INEP e IBGE, mas essas informações estão distribuídas em diferentes bases, formatos e publicações.

O Educadata propõe organizar esses dados em uma camada analítica única, com visualizações intuitivas e filtros que permitam compreender tendências nacionais e diferenças regionais e sociodemográficas.

OBJETIVOS:

- OBJETIVO GERAL: construir uma solução de análise e visualização de dados capaz de apoiar o monitoramento da evasão e do abandono escolar no Brasil.

OBJETIVO ESPECÍFICO:

- Consolidar indicadores educacionais provenientes de fontes oficiais.
- Explorar a evolução temporal do abandono e da evasão.
- Comparar regiões, estados, municípios e grupos de estudantes quando houver dados disponíveis e comparáveis.
- Investigar fatores associados ao abandono escolar.
- Incorporar indicadores complementares, como aprovação, reprovação, IDEB e infraestrutura escolar.
- Evidenciar limitações, lacunas e diferenças metodológicas das bases utilizadas.
- Disponibilizar uma interface que facilite a leitura dos resultados por públicos técnicos e não técnicos.

PÚBLICO - ALVO:

- Gestores e profissionais da educação;
- pesquisadores, estudantes e cientistas de dados;
- órgãos públicos e formuladores de políticas;
- jornalistas e organizações da sociedade civil;
- cidadãos interessados em educação pública.

INDICADORES PREVISTOS: O dashboard poderá contemplar, conforme disponibilidade e comparabilidade das bases ->

- taxa de abandono/evasão escolar;
- evolução temporal dos indicadores;
- aprovação e reprovação;
- distorção idade-série;
- IDEB;
- infraestrutura das escolas;
- características das redes de ensino;
- recortes territoriais e sociodemográficos;
- motivos associados à interrupção dos estudos, quando disponíveis em fontes oficiais ou pesquisas metodologicamente adequadas.

*IMPORTANTE: abandono, evasão e demais conceitos não devem ser tratados como sinônimos automaticamente. Cada indicador será apresentado com sua definição, período de referência e fonte.

LIMITAÇÕES E CUIDADOS:

- Algumas regiões podem apresentar baixa disponibilidade ou qualidade de dados.
- Existem municípios e períodos com pesquisas insuficientes.
- Mudanças metodológicas entre edições das bases podem afetar comparações históricas.
- Indicadores agregados podem esconder diferenças importantes entre grupos.
- Correlação entre fatores e abandono não implica causalidade.
- Dados confidenciais não serão publicados no dashboard.

METODOLOGIA:

O desenvolvimento seguirá um fluxo reprodutível:

1. Entendimento do problema: definição das perguntas de negócio e dos indicadores.
2. Aquisição: coleta das bases oficiais e documentação das versões.
3. Preparação: limpeza, padronização, tratamento de ausências e validação.
4. Integração: combinação de bases por chaves compatíveis, como território, ano e rede de ensino.
5. Análise exploratória: estatísticas descritivas, tendências, comparações e identificação de outliers.
6. Análise de fatores: investigação de associações entre abandono e variáveis disponíveis.
7. Visualização: construção de gráficos e indicadores interativos orientados às perguntas do público.
8. Validação: conferência dos resultados contra as fontes originais e testes de consistência.
9. Comunicação: documentação das interpretações, limitações e conclusões.

ESTRUTURA DO PROJETO --->

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



QUALIDADE E VALIDAÇÃO

Antes de promover alterações para `main`, devem ser verificadas:

- consistência dos dados;
- ausência de duplicidades indevidas;
- tratamento documentado de valores ausentes;
- compatibilidade de períodos e definições;
- coerência dos indicadores com as fontes oficiais;
- funcionamento das visualizações e filtros;
- atualização correta da documentação.
