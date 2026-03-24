# Diagnóstico de Qualidade - Startup Local Eats

## 1. Diagnóstico da Situação Atual

Com base no cenário apresentado, a startup Local Eats provavelmente tem uma equipe enxuta, com foco em entregar funcionalidades rapidamente, mas sem uma estrutura clara de qualidade.

### 1.1 Papéis que provavelmente existem hoje
- Desenvolvedor(a)
- Analista de Sistemas (ou pessoa de produto acumulando análise)
- Gerente de Produto (Product Manager)
- Suporte/Atendimento (informalmente trazendo feedback dos clientes)

Observação: pode não existir um papel formal de QA, ou ele pode ser exercido parcialmente por desenvolvedores.

### 1.2 Quem provavelmente está responsável pela qualidade atualmente
Atualmente, a qualidade parece estar distribuída de forma não planejada, com maior peso nos desenvolvedores e validações de última hora por produto/negócio. Isso gera um modelo reativo (corrigir depois que quebra), em vez de preventivo.

### 1.3 Problemas quando responsabilidades de qualidade não estão claras
- Falhas críticas chegam à produção
- Duplicidade de pedidos e inconsistência de dados
- Retrabalho alto e custo maior de correção
- Conflitos entre áreas sobre "quem deveria ter validado"
- Falta de rastreabilidade dos defeitos
- Queda de confiança de clientes e restaurantes

### 1.4 A qualidade é de uma pessoa ou da equipe?
A qualidade deve ser responsabilidade compartilhada de toda a equipe. Mesmo com um papel específico de QA, qualidade não é etapa final: ela deve ser construída desde requisitos, desenvolvimento, testes, deploy e monitoramento.

## 2. Papéis da Equipe

### Papel: Desenvolvedor(a)
Responsabilidades principais:
- Implementar funcionalidades com foco em código limpo e testável
- Criar testes unitários e apoiar testes de integração
- Corrigir defeitos com prioridade acordada

Relação com qualidade:
- Responsável por prevenir defeitos na origem e garantir critérios técnicos de qualidade no código.

### Papel: QA / Analista de Qualidade
Responsabilidades principais:
- Planejar e executar testes funcionais e exploratórios
- Definir critérios de aceitação testáveis com produto e análise
- Registrar, priorizar e acompanhar defeitos

Relação com qualidade:
- Atua como facilitador da qualidade, garantindo cobertura de testes e visibilidade de riscos antes da entrega.

### Papel: Analista de Sistemas
Responsabilidades principais:
- Elicitar e detalhar requisitos funcionais e não funcionais
- Garantir clareza de regras de negócio e critérios de aceite
- Apoiar validação de escopo com stakeholders

Relação com qualidade:
- Reduz ambiguidades de requisito, evitando defeitos gerados por interpretação incorreta.

### Papel: DevOps
Responsabilidades principais:
- Estruturar pipelines de CI/CD com validações automáticas
- Garantir ambientes consistentes (dev/homologação/produção)
- Monitorar estabilidade, logs e incidentes em produção

Relação com qualidade:
- Garante qualidade operacional, releases confiáveis e resposta rápida a falhas.

### Papel: Product Manager (ou Product Owner)
Responsabilidades principais:
- Priorizar backlog considerando valor e risco
- Aprovar critérios de aceite e definição de pronto
- Balancear velocidade de entrega com qualidade

Relação com qualidade:
- Direciona decisões para evitar débito técnico excessivo e entregas sem validação.

## 3. Responsabilidades Relacionadas a Qualidade

| Atividade de Qualidade | Responsável Primário | Apoio |
| :--- | :--- | :--- |
| Revisar requisitos e critérios de aceite | Analista de Sistemas | PM, QA |
| Planejar cenários de teste | QA | Analista, Dev |
| Executar testes manuais das funcionalidades críticas | QA | Dev |
| Criar e manter testes unitários | Desenvolvedor | QA |
| Registrar e acompanhar bugs | QA | Time inteiro |
| Revisar código (code review) | Desenvolvedor (pares) | Tech Lead |
| Validar funcionalidade antes de produção | QA | PM, Analista |
| Automatizar pipeline de validação (build/testes) | DevOps | Dev |
| Monitorar erros em produção e incidentes | DevOps | Dev, QA |

## 4. Práticas de QA Sugeridas

1. Definição de Pronto (DoD) com critério mínimo de qualidade
Todo item só pode ser entregue com critérios de aceite atendidos, testes executados e sem defeitos críticos abertos.

2. Testes manuais regressivos nas funcionalidades principais
Criar uma suíte enxuta de regressão para fluxo de pedido: seleção, pagamento, confirmação e recebimento do pedido pelo restaurante.

3. Registro e triagem semanal de defeitos
Manter backlog de bugs priorizado por severidade e impacto no negócio, com responsáveis e prazo.

4. Code review obrigatório antes de merge
Exigir revisão por pares para evitar defeitos lógicos, inconsistências e problemas de manutenção.

5. Monitoramento pós-release com checklist de estabilidade
Após deploy, acompanhar métricas de erro, pedidos duplicados e falhas de finalização para resposta rápida.

## 5. Anúncios de Contratação

### 5.1 Vaga 1 - Analista de Qualidade de Software (QA)

Informações do anúncio:
- Empresa: Local Eats
- Local: Porto Alegre - RS
- Modelo: Híbrido

Título da vaga:
- Analista de Qualidade de Software (QA)

Descrição da vaga:
A Local Eats busca profissional de QA para fortalecer a qualidade da plataforma de pedidos online. A pessoa atuará junto a desenvolvimento, análise e produto para prevenir falhas e garantir entregas confiáveis para clientes e restaurantes parceiros.

Principais responsabilidades:
- Planejar e executar testes funcionais
- Realizar testes exploratórios em fluxos críticos
- Identificar, registrar e acompanhar defeitos
- Apoiar definição de critérios de aceite
- Validar funcionalidades antes da liberação

Requisitos obrigatórios:
- Conhecimento básico/intermediário em testes de software
- Capacidade de documentar defeitos com clareza
- Noções de ciclo de desenvolvimento de software
- Boa comunicação e colaboração em equipe

Requisitos desejáveis:
- Experiência com testes em aplicações web
- Conhecimento em ferramentas de gestão de bugs
- Noções de testes de API e automação
- Conhecimento de Git

Certificações ou cursos relevantes:
- ISTQB CTFL (desejável)
- Cursos de testes funcionais e exploratórios

### 5.2 Vaga 2 - Desenvolvedor(a) Full Stack

Informações do anúncio:
- Empresa: Local Eats
- Local: Porto Alegre - RS
- Modelo: Híbrido ou Remoto

Título da vaga:
- Desenvolvedor(a) Full Stack

Descrição da vaga:
A Local Eats procura Desenvolvedor(a) Full Stack para atuar na evolução da plataforma de pedidos. A pessoa será responsável por implementar funcionalidades com qualidade, colaborar com QA e garantir estabilidade dos fluxos de compra.

Principais responsabilidades:
- Desenvolver e manter funcionalidades front-end e back-end
- Criar testes unitários para componentes e serviços
- Corrigir bugs priorizados pela equipe
- Participar de code reviews e melhorias técnicas
- Colaborar com DevOps no processo de integração contínua

Requisitos obrigatórios:
- Experiência com desenvolvimento web
- Conhecimento em APIs REST
- Conhecimento em banco de dados relacional
- Versionamento com Git
- Noções de testes automatizados

Requisitos desejáveis:
- Experiência com arquitetura de microsserviços
- Conhecimento em pipelines CI/CD
- Experiência com monitoramento e observabilidade

Certificações ou cursos relevantes:
- Cursos de desenvolvimento web moderno
- Cursos de testes automatizados
- Cursos de boas práticas de engenharia de software

---
Wesley Solisnande Santos Zorzolli - 24/03/2026