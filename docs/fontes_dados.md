# Catálogo de fontes de dados

Este catálogo registra as fontes oficiais priorizadas e o papel de cada uma no Educadata.

| Instituição | Base/indicador | Referência atual disponível | Uso no projeto | Status |
|---|---|---|---|---|
| INEP | Taxas de rendimento escolar | 2024; página oficial também disponibiliza séries históricas e atualização de 2025 | abandono, aprovação e reprovação | Fonte prioritária |
| INEP | Indicadores Educacionais | 2024/2025 conforme indicador | distorção idade-série, infraestrutura/contexto e outros indicadores | Fonte prioritária |
| INEP | Censo Escolar – resultados | 2025 e séries históricas | contexto escolar e validação dos indicadores | Fonte prioritária |
| INEP | IDEB | ciclo 2023 e séries anteriores | indicador complementar de qualidade | Fonte prioritária |
| IBGE | PNAD Contínua – Educação | 2024 | abandono de 14 a 29 anos, escolarização e recortes sociodemográficos | Fonte prioritária |

## Referências oficiais

- INEP — Indicadores Educacionais: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
- INEP — Taxas de Rendimento Escolar: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar
- INEP — Resultados do Censo Escolar: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/resultados
- INEP — Sinopses Estatísticas da Educação Básica: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/sinopses-estatisticas/educacao-basica
- IBGE — PNAD Contínua: https://www.ibge.gov.br/estatisticas/sociais/populacao/17270-pnad-

## Por que combinar INEP e IBGE?

O INEP é a fonte principal para indicadores derivados do sistema escolar, enquanto a PNAD Contínua do IBGE permite observar a condição de estudo e o abandono a partir da população, inclusive com recortes sociodemográficos. Essas medidas não devem ser somadas ou tratadas como equivalentes: o dashboard exibirá a definição, população, período e fonte de cada indicador.

## Critérios de inclusão

Uma fonte só entra na camada analítica após verificar:

1. autoria institucional e origem oficial;
2. documentação/metodologia disponível;
3. período de referência;
4. definição das variáveis;
5. cobertura territorial e populacional;
6. compatibilidade com as demais bases;
7. regras de acesso e redistribuição;
8. riscos de interpretação ou quebra de comparabilidade histórica.

## Rastreabilidade

Cada conjunto processado deve preservar a referência da fonte original, data de acesso e transformações aplicadas. Quando uma base não puder ser redistribuída, o repositório deve conter apenas scripts, metadados e instruções para obtenção legítima.
