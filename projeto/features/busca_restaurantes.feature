Feature: Buscar restaurantes por categoria
  Como cliente do LocalEats
  Quero fazer login e filtrar restaurantes por culinária
  Para encontrar opções de acordo com meu desejo

  Scenario: Fazer login e filtrar restaurantes japoneses
    Dado que estou na página inicial do LocalEats
    Quando eu faço login com o email "teste@teste.com" e a senha "123456"
    E eu aplico o filtro "Japonesa"
    Então eu devo ver restaurantes de comida japonesa listados

  Scenario: Visualizar restaurantes japoneses após autenticação
    Dado que estou na página inicial do LocalEats
    Quando eu já estou autenticado no LocalEats
    E eu aplico o filtro "Japonesa"
    Então eu devo ver restaurantes de comida japonesa listados
