# Aula 5 - Testes Funcionais vs Estruturais
## LocalEats

## Integrantes do Grupo
- Wesley Solisnande Santos Zorzolli

## 1. Funcionalidade escolhida

A funcionalidade escolhida foi a **busca de restaurantes**.

Ela serve para ajudar o usuário a encontrar opções mais rápido, usando um termo de pesquisa e filtros como tipo de culinária, preço e distância. O que se espera é simples: mostrar resultados compatíveis com o que foi pedido e não confundir quem está usando o app.

## 2. Testes Caixa-Preta (Visão do Usuário)

Sem olhar o código, eu testaria a busca em situações reais de uso para ver se o que aparece na tela bate com o que foi pedido.

### Entradas possíveis
- Buscar por um termo simples, como "pizza" ou "japonês"
- Usar termo e filtros ao mesmo tempo, como culinária, preço e distância
- Fazer uma busca sem preencher nenhum campo
- Alterar os filtros durante a pesquisa

### Comportamentos esperados
- O sistema deve retornar restaurantes relacionados ao termo informado
- Os filtros precisam ser respeitados, sem mostrar opções que fujam do critério escolhido
- Quando não houver resultado, o sistema deve avisar isso de forma clara
- Ao mudar um filtro, os resultados precisam ser atualizados

### Situações de erro que podem aparecer
- Restaurantes que não atendem ao filtro continuam aparecendo
- A lista mostra resultados inconsistentes ou fora de ordem
- A tela não atualiza depois que o usuário altera um filtro
- A busca retorna vazio mesmo quando deveria haver opções compatíveis

Esse tipo de teste ajuda a perceber falhas visíveis, principalmente as que atrapalham o uso normal da plataforma.

## 3. Testes Caixa-Branca (Visão do Sistema)

Agora, olhando para dentro do sistema, dá para imaginar que a busca tenha algumas validações antes de devolver os resultados.

### Possíveis estruturas lógicas internas
- Verificação se o campo de busca foi preenchido ou não
- Validação dos filtros escolhidos pelo usuário
- Consulta somente em restaurantes ativos ou disponíveis
- Aplicação das regras de distância, preço e tipo de culinária
- Ordenação final da lista antes de mostrar os resultados

### Situações que precisam ser testadas no código
- Caminhos em que o termo de busca existe e em que ele não existe
- Casos com um filtro isolado e com vários filtros ao mesmo tempo
- Regras que dependem de localização
- Situações de empate na ordenação
- Respostas quando não há restaurantes compatíveis com a regra interna

Esse olhar ajuda a identificar onde a lógica pode estar falhando. Um resultado incorreto pode vir de uma condição mal escrita, de uma validação incompleta ou de uma regra aplicada no momento errado.

## 4. Comparação entre as abordagens

A principal diferença é que, na caixa-preta, o teste é feito sem conhecer o código; na caixa-branca, o foco está em como o sistema foi construído.

A caixa-preta mostra o efeito do problema para o usuário. A caixa-branca ajuda a encontrar a causa técnica.

Na prática, cada uma encontra problemas diferentes: a caixa-preta pega falhas visíveis e a caixa-branca pega erros de lógica e caminhos internos não cobertos.

## 5. Reflexão no contexto do LocalEats

No cenário atual do LocalEats, as duas abordagens são úteis, mas nenhuma sozinha resolve tudo.

A caixa-preta é mais imediata para os problemas citados, porque mostra o erro na visão do usuário. Mas ela sozinha não explica por que isso acontece.

A caixa-branca ajuda a investigar a lógica interna e achar a origem da falha.

Por isso, o melhor é combinar as duas. Uma mostra o problema e a outra ajuda a entender a causa.

## Conclusão

Os testes funcionais e estruturais se complementam. No LocalEats, olhar para a funcionalidade pelas duas visões aumenta a chance de encontrar falhas reais.

Wesley Solisnande Santos Zorzolli - 06/04/2026