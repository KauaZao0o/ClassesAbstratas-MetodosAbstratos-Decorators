"""Exercício 3: decorator para registrar a execução de funções."""

from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast


F = TypeVar("F", bound=Callable[..., Any])


def registrar_execucao(funcao: F) -> F:
    """Exibe mensagens antes e depois da execução de ``funcao``."""

    @wraps(funcao)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Iniciando execução...")
        print(f"Função: {funcao.__name__}")
        try:
            return funcao(*args, **kwargs)
        finally:
            print("Execução finalizada.")

    return cast(F, wrapper)


@registrar_execucao
def enviar_email(destinatario: str) -> None:
    """Simula o envio de um e-mail."""
    print(f"E-mail enviado para {destinatario}")


@registrar_execucao
def gerar_relatorio(nome: str) -> None:
    """Simula a geração de um relatório."""
    print(f"Relatório '{nome}' gerado.")
