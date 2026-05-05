from decimal import Decimal

import pytest

from src.pedido import calcular_total_pedido


def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 30

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == Decimal("30")


def test_deve_calcular_total_quando_valor_minimo_e_ultrapassado():
    itens = [{"preco": 25}, {"preco": 15}, {"preco": 10}]
    valor_minimo = 40

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == Decimal("50")


def test_deve_gerar_erro_quando_valor_minimo_nao_for_atingido():
    itens = [{"preco": 8}, {"preco": 7}]
    valor_minimo = 20

    with pytest.raises(ValueError, match="Valor minimo do pedido nao atingido"):
        calcular_total_pedido(itens, valor_minimo)


def test_deve_gerar_erro_quando_lista_de_itens_esta_vazia():
    with pytest.raises(ValueError, match="O pedido deve conter pelo menos um item"):
        calcular_total_pedido([], 10)


def test_deve_gerar_erro_quando_preco_do_item_e_negativo():
    itens = [{"preco": 10}, {"preco": -1}]

    with pytest.raises(ValueError, match="Preco do item 2 nao pode ser negativo"):
        calcular_total_pedido(itens, 5)


def test_deve_calcular_total_com_valores_decimais_sem_perda_de_precisao():
    itens = [{"preco": "10.10"}, {"preco": "5.25"}, {"preco": "4.65"}]
    valor_minimo = "20.00"

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == Decimal("20.00")
