# Dicionário inicial de indicadores

O dicionário define o contrato mínimo para qualquer indicador exibido pelo dashboard.

| Campo | Descrição |
|---|---|
| `indicador` | Nome padronizado do indicador |
| `valor` | Valor numérico do indicador |
| `ano` | Ano/período de referência |
| `territorio` | UF, município, região ou Brasil |
| `codigo_territorio` | Código territorial quando disponível |
| `rede` | Dependência/rede de ensino, quando aplicável |
| `etapa` | Etapa/modalidade de ensino, quando aplicável |
| `populacao_referencia` | População sobre a qual o indicador foi calculado |
| `fonte` | Instituição responsável |
| `base` | Nome da pesquisa/base |
| `definicao` | Definição metodológica resumida |
| `cobertura` | Cobertura territorial/populacional conhecida |

## Indicadores prioritários

### Taxa de abandono

Indicador de rendimento escolar produzido a partir das informações de movimento e rendimento do Censo Escolar. Deve ser armazenado com ano, etapa, rede e território para permitir comparações compatíveis.

### Aprovação e reprovação

Indicadores de rendimento utilizados para contextualizar o abandono e compor análises de fluxo escolar.

### Distorção idade-série

Indicador complementar para identificar situações em que a idade do estudante está defasada em relação à etapa adequada, respeitando a definição e a metodologia oficiais da edição utilizada.

### IDEB

Indicador complementar de qualidade que combina desempenho em avaliação padronizada e rendimento escolar. Não deve ser interpretado como medida direta de evasão.

### Abandono na pop

Medida proveniente de pesquisas domiciliares, como a PNAD Contínua, com população de referência própria. Deve permanecer separada dos indicadores administrativos do Censo Escolar.

## Regras de apresentação

1. Todo valor exibido deve ter fonte e período.
2. Indicadores de fontes diferentes não devem ser colocados na mesma série sem compatibilidade metodológica.
3. Ausência de valor deve aparecer como ausência de dado, e não como zero.
4. Alterações metodológicas relevantes devem ser sinalizadas no dashboard.
5. Diferenças entre grupos devem ser acompanhadas da população e do período de referência.
