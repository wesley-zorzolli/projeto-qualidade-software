# Aula 9 - Testes Unitarios Automatizados e TDD

## Integrante
- Wesley Solisnande Santos Zorzolli

---

## 1. Funcionalidade escolhida

### Calculo do total do pedido com valor minimo

Arquivos usados:
- src/pedido.py
- tests/test_pedido.py

O que essa funcionalidade faz:
- soma o preco dos itens do pedido;
- valida se atingiu o valor minimo do restaurante;
- gera erro quando o pedido e invalido.

Regras de negocio aplicadas:
- total = soma dos itens;
- se total < valor minimo, retorna erro;
- lista vazia retorna erro;
- preco negativo retorna erro.

---

## 2. Testes Unitarios

Implementei 6 testes no total.

### Teste 1 - valor minimo atingido (sucesso)
- Cenario: soma igual ao minimo.
- Entrada: 10 + 20, minimo 30.
- Esperado: retorna 30.

```python
def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 30
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == Decimal("30")
```

### Teste 2 - valor minimo ultrapassado (sucesso)
- Cenario: soma acima do minimo.
- Entrada: 25 + 15 + 10, minimo 40.
- Esperado: retorna 50.

```python
def test_deve_calcular_total_quando_valor_minimo_e_ultrapassado():
    itens = [{"preco": 25}, {"preco": 15}, {"preco": 10}]
    valor_minimo = 40
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == Decimal("50")
```

### Teste 3 - abaixo do valor minimo (erro)
- Cenario: pedido invalido.
- Entrada: 8 + 7, minimo 20.
- Esperado: ValueError.

```python
def test_deve_gerar_erro_quando_valor_minimo_nao_for_atingido():
    itens = [{"preco": 8}, {"preco": 7}]
    with pytest.raises(ValueError, match="Valor minimo do pedido nao atingido"):
        calcular_total_pedido(itens, 20)
```

### Testes extras (borda)
- lista de itens vazia -> erro;
- item com preco negativo -> erro;
- soma com decimais -> resultado exato.

---

## 3. Aplicacao do TDD

### Red
Primeiro escrevi o teste com a funcao ainda incompleta. Exemplo inicial:

```python
def calcular_total_pedido(itens, valor_minimo):
    return 0
```

Com isso, o teste falhou.

### Green
Depois implementei o minimo para passar:
- somar os itens;
- validar contra o valor minimo.

### Refactor
Com os testes passando, melhorei:
- uso de Decimal para evitar problema com ponto flutuante;
- validacoes de entrada;
- mensagens de erro mais claras.

---

## 4. Refatoracao

Melhorias feitas:
- codigo ficou mais legivel separando conversao numerica em funcao auxiliar;
- validacoes ficaram mais organizadas;
- erros ficaram mais especificos, facilitando manutencao.

---

## 5. Execucao dos Testes

Resumo:
- Total de testes: 6
- Passaram: 6
- Falharam: 0

Comando executado:

```text
python -m pytest -q
```

Saida real:

```text
......                                                                   [100%]
6 passed in 0.05s
```

---

## 6. Reflexao (LocalEats)

Foi dificil escrever testes antes do codigo?
- No inicio sim, porque tive que pensar primeiro na regra.

O TDD ajudou no desenvolvimento?
- Sim, porque me guiou por etapas e evitou implementar coisa desnecessaria.

Os testes aumentaram a confianca no codigo?
- Sim, porque qualquer alteracao eu consigo validar rapido.

O que eu melhoraria?
- Aumentaria ainda mais os cenarios invalidos (ex.: campo preco ausente).

Como isso ajuda no projeto do grupo?
- Diminui regressao e deixa mais facil evoluir a regra de pedido com seguranca.

---

Wesley Solisnande Santos Zorzolli - 05 de maio de 2026
