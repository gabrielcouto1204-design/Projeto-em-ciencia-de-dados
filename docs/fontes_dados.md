# Catálogo de fontes de dados

Este catálogo registra as fontes oficiais priorizadas e o papel de cada uma no Educadata.

| Instituição | Base/indicador | Referência atual | Uso no projeto | Status |
|---|---|---|---|---|
| INEP | Taxas de Rendimento Escolar | Séries históricas disponíveis até 2025 | abandono, aprovação e reprovação | Prioritária |
| INEP | Censo Escolar | Microdados até 2025 | contexto escolar, matrícula, movimento e rendimento | Prioritária |
| INEP | Indicadores Educacionais | Séries conforme o indicador | distorção idade-série e indicadores complementares | Prioritária |
| INEP | IDEB | Séries históricas conforme ciclo | indicador complementar de qualidade | Prioritária |
| IBGE | PNAD Contínua – Educação | 2024 para o recorte de abandono usado nesta etapa | abandono, escolarização e recortes sociodemográficos | Prioritária |

## Referências oficiais

- INEP — Censo Escolar: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar
- INEP — Microdados do Censo Escolar: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
- INEP — Indicadores Educacionais: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
- INEP — Taxas de Rendimento Escolar: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar
- IBGE — PNAD Contínua: https://www.ibge.gov.br/estatisticas/sociais/populacao/17270-pnad-continua.html

## Papel de cada fonte

O **INEP** é a referência principal para indicadores derivados do sistema escolar. A segunda etapa do Censo Escolar coleta movimento e rendimento ao final do ano letivo e subsidia o cálculo das taxas de aprovação, reprovação e abandono. O **IBGE** complementa a análise com medidas da população, permitindo recortes sociodemográficos e uma perspectiva diferente do fenômeno.

Essas medidas não devem ser somadas ou tratadas como equivalentes. O dashboard deverá exibir definição, população de referência, período e fonte de cada indicador.

## Critérios de inclusão

Uma fonte só entra na camada analítica após verificar:

1. autoria institucional e origem oficial;
2. documentação e metodologia disponíveis;
3. período de referência;
4. definição das variáveis;
5. cobertura territorial e populacional;
6. compatibilidade com as demais bases;
7. regras de acesso e redistribuição;
8. riscos de interpretação ou quebra de comparabilidade histórica.

## Rastreabilidade

Para cada conjunto processado, registrar:

- instituição e nome da base;
- URL oficial;
- ano/período de referência;
- data de acesso;
- versão ou arquivo utilizado;
- transformações aplicadas;
- limitações conhecidas.

Quando uma base não puder ser redistribuída, o repositório deve conter somente scripts, metadados e instruções para obtenção legítima.

## Observação metodológica atualizada

O Inep informa que a Situação do Aluno reúne informações de rendimento e movimento e é utilizada no cálculo das taxas de rendimento e do Ideb. Para o exercício de 2027, uma nota técnica de 2026 propõe um indicador de atendimento baseado na permanência do estudante entre 2024 e 2025. Esse indicador não deve ser confundido automaticamente com a taxa de abandono tradicional; o Educadata manterá as definições separadas.
