# Catálogo de fontes de dados

Este documento será atualizado à medida que cada base oficial for incorporada ao pipeline.

| Fonte | Base/indicador | Período | Unidade | Uso no projeto | Status |
|---|---|---:|---|---|---|
| INEP | Censo Escolar / indicadores educacionais | A definir | Escola/rede/território | Abandono, aprovação, reprovação e contexto escolar | Em validação |
| INEP | IDEB | A definir | Escola/rede/território | Indicador complementar | Em validação |
| IBGE | Indicadores sociais, demográficos e educacionais | A definir | Município/UF/território | Contextualização territorial | Em validação |

## Critérios de inclusão

Uma fonte só entra na camada analítica após verificar:

1. autoria institucional e origem oficial;
2. documentação/metodologia disponível;
3. período de referência;
4. definição das variáveis;
5. cobertura territorial;
6. compatibilidade com as demais bases;
7. regras de acesso e redistribuição;
8. riscos de interpretação ou quebra de comparabilidade histórica.

## Rastreabilidade

Cada conjunto processado deve preservar a referência da fonte original e registrar as transformações aplicadas. Quando uma base não puder ser redistribuída, o repositório deve conter apenas scripts, metadados e instruções para obtenção legítima.
