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

## CT-04 - Login com senha inválida
**Pré-condição:** estar na tela de login.  
**Passos:** informar usuário válido, informar senha incorreta e clicar em entrar.  
**Dados de entrada:** usuário válido e senha inválida.  
**Resultado esperado:** acesso bloqueado e mensagem de erro na tela.

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
| CT-04 | Falhou | Ao tentar validar o login, apareceu a mensagem do navegador pedindo "@" no e-mail informado. Não foi possível concluir a validação de senha incorreta nesse teste. |
| CT-05 | Falhou | Não houve resultado, mas faltou uma mensagem clara de vazio. |

## Evidências observadas
- E01: autenticação funcionou corretamente.
- E02: a busca por "brasileira" trouxe resultados relevantes.
- E03: o carrinho atualizou como esperado.
- E04: no teste de login inválido, o campo de e-mail falhou na validação de formato antes da verificação de senha.
- E05: a busca sem resultado não foi comunicada direito.

---

# 4. Análise dos Resultados

Foram executados 5 testes: 3 passaram e 2 falharam.

Os principais problemas foram a validação de entrada no login (que impediu concluir o cenário de senha inválida) e a falta de feedback claro quando a busca não encontrou restaurantes. Nos fluxos de sucesso, a aplicação respondeu bem e sem erros críticos.

---

# 5. Reflexão no contexto do LocalEats

## O plano ajudou?
Sim. Ele me ajudou a não testar de forma aleatória e a organizar melhor o que eu iria observar.

## Algum problema apareceu só na execução?
Sim. Na prática ficou mais claro que o sistema funciona, mas comunica mal os erros e os estados sem resultado.

## O que eu melhoraria?
Eu adicionaria mais testes de entrada vazia, faria prints reais do que apareceu na tela e testaria em mais de um navegador, se desse.

## Conclusão
O LocalEats funcionou bem nos fluxos principais, mas ainda precisa melhorar os retornos de erro e de tela vazia.

---

Wesley Solisnande Santos Zorzolli - 14 de abril de 2026
