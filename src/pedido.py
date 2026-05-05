from decimal import Decimal, InvalidOperation
from typing import Iterable, Mapping


def _to_decimal(valor: object, campo: str) -> Decimal:
    """Converte entrada numerica para Decimal com mensagem de erro amigavel."""
    try:
        return Decimal(str(valor))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"{campo} invalido") from exc


def calcular_total_pedido(itens: Iterable[Mapping[str, object]], valor_minimo: object) -> Decimal:
    """Soma os itens do pedido e valida se o valor minimo foi atingido."""
    itens_lista = list(itens)

    if not itens_lista:
        raise ValueError("O pedido deve conter pelo menos um item")

    minimo = _to_decimal(valor_minimo, "Valor minimo")
    if minimo < 0:
        raise ValueError("Valor minimo nao pode ser negativo")

    total = Decimal("0")
    for indice, item in enumerate(itens_lista, start=1):
        if "preco" not in item:
            raise ValueError(f"Item {indice} sem campo preco")

        preco = _to_decimal(item["preco"], f"Preco do item {indice}")
        if preco < 0:
            raise ValueError(f"Preco do item {indice} nao pode ser negativo")

        total += preco

    if total < minimo:
        raise ValueError("Valor minimo do pedido nao atingido")

    return total
