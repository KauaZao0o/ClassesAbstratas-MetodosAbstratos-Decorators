"""Testes automatizados para os três exercícios."""

import io
import unittest
from contextlib import redirect_stdout

from decorators import gerar_relatorio
from funcionarios import Estagiario, Funcionario, FuncionarioCLT, FuncionarioComissionado
from pagamento import Pagamento, PagamentoCartao, PagamentoPix


class TestPagamentos(unittest.TestCase):
    def test_pagamento_abstrato_nao_pode_ser_instanciado(self) -> None:
        with self.assertRaises(TypeError):
            Pagamento(100)  # type: ignore[abstract]

    def test_subclasses_implementam_processamento(self) -> None:
        pix = PagamentoPix(100)
        cartao = PagamentoCartao(200, "1234")

        self.assertEqual(pix.valor, 100)
        self.assertEqual(cartao.valor, 200)
        self.assertEqual(cartao.numero_cartao, "1234")


class TestFuncionarios(unittest.TestCase):
    def test_funcionario_abstrato_nao_pode_ser_instanciado(self) -> None:
        with self.assertRaises(TypeError):
            Funcionario("Pessoa", 1000)  # type: ignore[abstract]

    def test_calculo_clt(self) -> None:
        funcionario = FuncionarioCLT("Ana", 3500, 500)
        self.assertEqual(funcionario.calcular_salario(), 4000)

    def test_calculo_comissionado(self) -> None:
        funcionario = FuncionarioComissionado("Bruno", 2000, 25000, 5)
        self.assertEqual(funcionario.calcular_salario(), 3250)

    def test_calculo_estagiario(self) -> None:
        estagiario = Estagiario("Carla", 1200, 250)
        self.assertEqual(estagiario.calcular_salario(), 1450)


class TestDecorator(unittest.TestCase):
    def test_decorator_exibe_mensagens_e_aceita_kwargs(self) -> None:
        saida = io.StringIO()

        with redirect_stdout(saida):
            gerar_relatorio(nome="Vendas")

        self.assertEqual(
            saida.getvalue().splitlines(),
            [
                "Iniciando execução...",
                "Função: gerar_relatorio",
                "Relatório 'Vendas' gerado.",
                "Execução finalizada.",
            ],
        )


if __name__ == "__main__":
    unittest.main()
