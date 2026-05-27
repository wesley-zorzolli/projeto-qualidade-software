# Aula 6 - Planejamento e Execução de Testes

## Integrante
- Wesley Solisnande Santos Zorzolli

---

# 1. Plano de Testes

## Objetivo
Organizar testes simples para o LocalEats e verificar se os fluxos principais funcionam como esperado.

## Escopo
O que eu testei:
- login e autenticação
- busca de restaurantes
- visualização de detalhes
- início de pedido
- mensagens de erro

O que eu não testei:
- pagamento real
- entrega
- segurança avançada
- desempenho com muita carga
- compatibilidade completa com outros navegadores
- testes automatizados

## Funcionalidades escolhidas
- login
- busca
- pedido
- avaliação

## Estratégia
Usei testes funcionais, caixa-preta e uma verificação básica de usabilidade. Montei os casos antes e fiz a execução de forma manual, simulando o que dava para observar no sistema.

## Responsável
| Nome | Responsabilidade |
|------|------------------|
| Wesley Solisnande Santos Zorzolli | Planejamento, execução e registro dos resultados |

---

# 2. Casos de Teste

## CT-01 - Login com sucesso
**Pré-condição:** estar na tela de login.  
**Passos:** informar usuário válido, informar senha correta e clicar em entrar.  
**Dados de entrada:** usuário válido e senha válida.  
**Resultado esperado:** acesso liberado e página principal aberta.

## CT-02 - Buscar restaurante existente
**Pré-condição:** estar autenticado.  
**Passos:** usar o campo de busca, digitar um termo existente e executar a busca.  
**Dados de entrada:** termo "brasileira".  
**Resultado esperado:** exibir restaurantes compatíveis.

## CT-03 - Iniciar pedido com item válido
**Pré-condição:** estar autenticado e com cardápio aberto.  
**Passos:** selecionar um item, adicionar ao pedido e avançar.  
**Dados de entrada:** item disponível no cardápio do restaurante.  
**Resultado esperado:** item aparece no resumo e o sistema permite continuar.

## CT-04 - Login com e-mail inválido
**Pré-condição:** estar na tela de login.  
**Passos:** informar e-mail em formato inválido, informar senha qualquer e clicar em entrar.  
**Dados de entrada:** e-mail sem "@" e senha qualquer.  
**Resultado esperado:** acesso bloqueado e validação de formato de e-mail exibida na tela.

## CT-05 - Buscar restaurante inexistente
**Pré-condição:** estar autenticado.  
**Passos:** usar o campo de busca, digitar um termo sem resultado e executar a busca.  
**Dados de entrada:** termo sem correspondência, como "XYZRestaurante999".  
**Resultado esperado:** informar que não há restaurantes encontrados.

---

# 3. Execução dos Testes

Eu simulei a execução no LocalEats pelo navegador em https://local-eats-unisenac.vercel.app/.

| ID | Resultado | Evidência |
|----|-----------|-----------|
| CT-01 | Passou | Login válido abriu a página `/home` e exibiu o menu principal. |
| CT-02 | Passou | A busca por "brasileira" retornou restaurantes com comida brasileira. |
| CT-03 | Passou | O item selecionado entrou no resumo do pedido. |
| CT-04 | Passou | O sistema bloqueou o envio e exibiu validação de e-mail inválido (exigindo formato com "@"). |
| CT-05 | Falhou | Não houve resultado, mas faltou uma mensagem clara de vazio. |

## Evidências observadas
- E01: autenticação funcionou corretamente.
- E02: a busca por "brasileira" trouxe resultados relevantes.
- E03: o carrinho atualizou como esperado.
- E04: no teste de e-mail inválido, o formulário bloqueou o envio e mostrou validação de formato.
- E05: a busca sem resultado não foi comunicada direito.

## Registro de evidências
- Evidência textual consolidada nesta seção de execução (resultado e descrição por caso).
- Recomendação para evolução: anexar capturas de tela por caso em `artefatos/evidencias/` para reforçar rastreabilidade.

---

# 4. Análise dos Resultados

Foram executados 5 testes: 3 passaram e 2 falharam.

Os principais problemas encontrados foram a ausência de feedback claro quando a busca não encontrou restaurantes e limitações de comunicação de estado da interface em cenários de erro. Nos fluxos de sucesso, a aplicação respondeu bem e sem erros críticos.

---

# 5. Reflexão no contexto do LocalEats

## O plano ajudou?
Sim. Ele me ajudou a não testar de forma aleatória e a organizar melhor o que eu iria observar.

## Algum problema apareceu só na execução?
Sim. Na prática ficou mais claro que o sistema funciona, mas comunica mal os erros e os estados sem resultado.

## O que eu melhoraria?
Eu adicionaria mais testes de entrada vazia, anexaria prints por caso para aumentar rastreabilidade e testaria em mais de um navegador.

## Conclusão
O LocalEats funcionou bem nos fluxos principais, mas ainda precisa melhorar os retornos de erro e de tela vazia.

---

Wesley Solisnande Santos Zorzolli - 14 de abril de 2026
