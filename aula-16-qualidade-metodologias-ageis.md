# Aula 16 – Qualidade em Metodologias Ágeis

## Integrantes

* Wesley Solisnande Santos Zorzolli

## 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
| :--- | :--- | :--- | :--- |
| **Planejamento iterativo** | Sim | O desenvolvimento do LocalEats ocorre de forma particionada acompanhando o cronograma e os prazos das entregas letivas estabelecidas no PBL[cite: 2]. | **Sim.** Pode ser formalizado definindo iterações menores e fixas (Sprints de 1 a 2 semanas)[cite: 1], desvinculando o ritmo apenas das datas finais acadêmicas. |
| **Priorização de funcionalidades** | Parcialmente | Os requisitos são priorizados de forma intuitiva, focando primeiro no que é obrigatório para a validação mínima do projeto[cite: 2]. | **Sim.** Pode ser melhorada utilizando frameworks de ordenação de Backlog, como a matriz MoSCoW, maximizando o valor de negócio antes de codificar[cite: 1]. |
| **Entregas incrementais** | Sim | A cada nova etapa do projeto, novos módulos funcionais e telas (como o catálogo e os fluxos de restaurante) são integrados ao sistema[cite: 2]. | **Sim.** Garantindo que cada incremento gerado possua testes funcionais e de aceitação acoplados, evitando empilhar código sem validação robusta[cite: 1]. |
| **Feedback frequente** | Parcialmente | Ocorre em momentos específicos de revisão com o professor Luciano Zanuz atuando como cliente/PO durante os alinhamentos em sala[cite: 2]. | **Sim.** Estabelecendo loops de feedback mais curtos, validando incrementos de interface e usabilidade diretamente com usuários[cite: 1]. |
| **Trabalho colaborativo** | Sim | O desenvolvimento é focado na integração contínua do repositório e alinhamento constante dos objetivos da unidade curricular[cite: 2]. | **Sim.** Como o trabalho é individual, a colaboração foca na revisão cruzada de código com outros colegas ou uso de técnicas como pair programming em momentos de mentoria[cite: 1]. |
| **Controle visual das atividades** | Parcialmente | Depende essencialmente do controle pessoal e da visualização de commits e pull requests abertos diretamente no GitHub[cite: 2]. | **Sim.** Implementando um quadro Kanban estruturado (no GitHub Projects), que ofereça visibilidade total e centralizada sobre o andamento do fluxo[cite: 1, 2]. |
| **Melhoria contínua** | Parcialmente | O processo é ajustado de forma reativa à medida que problemas de design de código ou gargalos de prazo surgem na proximidade das entregas[cite: 2]. | **Sim.** Adotando autoavaliações rápidas ao fim de cada ciclo para analisar as práticas de engenharia, e não apenas o software produzido[cite: 1]. |

### Conclusão

Os principais pontos fortes do desenvolvimento individual do LocalEats baseiam-se na agilidade de tomada de decisão e na constância em realizar as entregas incrementais funcionais exigidas pelo PBL[cite: 2]. Em contrapartida, as maiores oportunidades de melhoria residem na transição de um fluxo empírico e sob demanda para uma engenharia de software mais disciplinada e visual[cite: 1]. A falta de rituais ágeis bem delimitados e de métricas visuais eleva o risco do antipadrão *Go Horse* próximo aos prazos finais das entregas[cite: 1]. Estruturar formalmente o fluxo com controle de tarefas e portões de qualidade reduzirá a dívida técnica acumulada, garantindo alta velocidade aliada à excelência contínua[cite: 1].

## 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
| :--- | :--- | :--- |
| **Utilizar um quadro Kanban com limite de WIP (Work in Progress)** | Kanban | Aumentar a visibilidade das tarefas em andamento, identificar gargalos ocultos e forçar a conclusão das pendências abertas antes de iniciar novos códigos[cite: 1, 2]. |
| **Adotar Code Review sistemático via Pull Requests** | XP (Extreme Programming) | Manter a aderência aos padrões de Clean Code, interceptar defeitos ocultos antes de mesclar na branch principal e criar um histórico técnico limpo[cite: 1]. |
| **Modelar critérios de aceitação com base em cenários Gherkin (BDD)** | Práticas de Teste Ágil / Scrum | Eliminar a ambiguidade na especificação dos requisitos das histórias de usuário, unificando o entendimento do comportamento esperado do sistema antes de codificar[cite: 1, 2]. |
| **Executar sessões programadas de Refatoração Contínua** | XP (Extreme Programming) | Promover o aperfeiçoamento contínuo da arquitetura e legibilidade do código-fonte do LocalEats sem alterar o comportamento externo, reduzindo os juros da dívida técnica[cite: 1]. |

## 3. Definition of Ready (DoR)

Uma funcionalidade estará pronta para desenvolvimento quando:

* **História de usuário estruturada:** O requisito possui uma descrição textual clara especificando o ator, a ação e o valor de negócio esperado ("Como um [ator], eu quero [ação], para que [benefício]")[cite: 1].
* **Critérios de aceitação validados:** As regras de negócio e limites de comportamento da funcionalidade estão explicitamente descritos[cite: 1, 2].
* **Mapeamento de dependências zerado:** Quaisquer dependências externas, bibliotecas ou pré-requisitos técnicos foram identificados e estão disponíveis[cite: 1].
* **Viabilidade técnica consensual:** A arquitetura da tarefa foi analisada e confirmada como executável dentro do escopo do projeto sem impedimentos tecnológicos conhecidos[cite: 1].
* **Esforço estimado:** O item do backlog foi devidamente dimensionado em termos de complexidade ou esforço antes do início do código[cite: 1].

## 4. Definition of Done (DoD)

Uma funcionalidade será considerada concluída quando:

* **Implementação e revisão executadas:** O código correspondente está integralmente desenvolvido, respeita os padrões de estilo estabelecidos (Coding Standards) e passou por autoinspeção ou revisão via Pull Request[cite: 1].
* **Critérios de aceitação validados:** O incremento foi testado e cumpre rigorosamente todos os cenários estipulados nos critérios de aceite do requisito[cite: 1, 2].
* **Integração limpa (CI):** O código foi integrado com sucesso ao branch principal do repositório no GitHub (`main`) sem quebrar funcionalidades existentes (garantia de não regressão)[cite: 1].
* **Ausência de bugs críticos:** Não existem defeitos impeditivos ou falhas funcionais em aberto associadas à alteração recém-introduzida[cite: 1].
* **Deploy efetuado:** A build automática foi gerada de forma bem-sucedida e o sistema atualizado está publicado e disponível no ambiente de homologação (Vercel)[cite: 1, 2].

Wesley Solisnande Santos Zorzolli - 18 de junho de 2026