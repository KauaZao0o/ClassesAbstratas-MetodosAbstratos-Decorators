"""Exercício 1: classes abstratas para um sistema de pagamentos."""

from abc import ABC, abstractmethod


class Pagamento(ABC):
    """Representa um pagamento que precisa ser processado por uma subclasse."""

    def __init__(self, valor: float) -> None:
        self.valor = valor

    def exibir_valor(self) -> None:
        """Exibe o valor associado ao pagamento."""
        print(f"Valor do pagamento: R$ {self.valor:.2f}")

    @abstractmethod
    def processar_pagamento(self) -> None:
        """Processa o pagamento de acordo com a forma escolhida."""


class PagamentoPix(Pagamento):
    """Pagamento realizado por PIX."""

    def processar_pagamento(self) -> None:
        print("Pagamento realizado via PIX.")


class PagamentoCartao(Pagamento):
    """Pagamento realizado com cartão."""

    def __init__(self, valor: float, numero_cartao: str) -> None:
        super().__init__(valor)
        self.numero_cartao = numero_cartao

    def processar_pagamento(self) -> None:
        print("Pagamento realizado via cartão.")
