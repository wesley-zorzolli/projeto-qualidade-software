# Aula 15 – Modelos de Maturidade

## Integrantes
- Wesley Solisnande Santos Zorzolli

---

# 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|---|:---:|:---:|:---:|
| 1. Controle de versão (Git/GitHub) | X |  |  |
| 2. Gerenciamento de requisitos documentado |  | X |  |
| 3. Planejamento de atividades e prazos |  | X |  |
| 4. Revisão de código por pares |  |  | X |
| 5. Integração contínua (CI) |  |  | X |
| 6. Testes automatizados (unitários/integração) |  |  | X |
| 7. Testes manuais executados e registrados |  | X |  |
| 8. Registro formal de bugs/issue tracking |  |  | X |
| 9. Métricas de qualidade automatizadas |  |  | X |
| 10. Controle formal de mudanças |  |  | X |
| 11. Documentação de arquitetura/sistema |  | X |  |
| 12. Rastreabilidade de requisitos |  |  | X |
| 13. Retrospectivas e melhorias contínuas |  |  | X |
| 14. Gerenciamento de riscos |  | X |  |

### Nível de maturidade estimado
Nível Inicial / Nível 1 do CMMI

### Justificativa
Por se tratar de um projeto individual, todo o processo depende exclusivamente do meu esforço e disponibilidade. Uso GitHub para versionamento, e documento requisitos de forma parcial, mas não há revisões por pares, nem controle formal de mudanças, nem registros sistemáticos de bugs ou métricas automatizadas. Os testes são basicamente manuais e executados por mim antes de subir funcionalidades, caracterizando um processo reativo e em estágio inicial.

---

# 2. Lacunas Identificadas

| Lacuna | Impacto |
|---|---|
| Ausência de revisão de código por outro desenvolvedor | Maior risco de introdução de erros não detectados e soluções subótimas; perda de oportunidade de aprendizagem por feedback. |
| Ausência de métricas de qualidade automatizadas | Dificuldade em medir evolução da qualidade e identificar regressões automaticamente; dependência de sensação subjetiva. |
| Testes 100% manuais sem registro de falhas | Baixa repetibilidade dos testes, risco de regressões não detectadas e histórico de erros não documentado. |

---

# 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| Criar uma pipeline simples de testes automatizados com GitHub Actions e `pytest` | Garante execução automática de testes a cada push/PR, reduz regressões e aumenta confiança nas entregas. |
| Usar as Issues do GitHub para organizar e registrar bugs, tarefas e mudanças | Permite rastrear histórico de problemas, priorizar correções e ter um registro formal mesmo trabalhando sozinho. |
| Integrar uma análise estática de código (ex.: SonarQube/SonarCloud ou linters via CI) | Ajuda a identificar problemas estruturais, dívida técnica e vulnerabilidades, suprindo parte da falta de revisão por pares. |

---

## Conclusão
Mesmo trabalhando sozinho é possível evoluir o processo com melhorias práticas e incrementais: automatizar testes básicos, usar o GitHub como backlog/registro e adicionar análise estática trazem disciplina e visibilidade sem exigir equipe extra. Pequenos passos contínuos reduzem riscos e tornam o projeto mais sustentável.
