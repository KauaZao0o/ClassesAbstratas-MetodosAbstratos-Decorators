"""Demonstração dos três exercícios propostos."""

from decorators import enviar_email, gerar_relatorio
from funcionarios import Estagiario, FuncionarioCLT, FuncionarioComissionado
from pagamento import Pagamento, PagamentoCartao, PagamentoPix


def demonstrar_pagamentos() -> None:
    print("=== Exercício 1: Sistema de Pagamentos ===")

    pagamento_pix = PagamentoPix(150.00)
    pagamento_pix.exibir_valor()
    pagamento_pix.processar_pagamento()

    print()
    pagamento_cartao = PagamentoCartao(320.50, "1234 5678 9012 3456")
    pagamento_cartao.exibir_valor()
    pagamento_cartao.processar_pagamento()

    print("\nDesafio: tentativa de instanciar Pagamento")
    try:
        Pagamento(100.00)  # type: ignore[abstract]
    except TypeError as erro:
        print(f"Não foi possível: {erro}")
        print(
            "Pagamento é abstrata e só pode ser instanciada por meio de uma "
            "subclasse que implemente processar_pagamento()."
        )


def demonstrar_funcionarios() -> None:
    print("\n=== Exercício 2: Funcionários de uma Empresa ===")

    funcionarios = [
        FuncionarioCLT("Ana", 3500.00, 500.00),
        FuncionarioComissionado("Bruno", 2000.00, 25000.00, 5.0),
        Estagiario("Carla", 1200.00, 250.00),
    ]

    for funcionario in funcionarios:
        print()
        funcionario.exibir_dados()
        print(f"Salário final: R$ {funcionario.calcular_salario():.2f}")


def demonstrar_decorator() -> None:
    print("\n=== Exercício 3: Decorator de Registro de Execução ===")
    enviar_email("cliente@email.com")
    print()
    gerar_relatorio(nome="Relatório de vendas")


if __name__ == "__main__":
    demonstrar_pagamentos()
    demonstrar_funcionarios()
    demonstrar_decorator()
