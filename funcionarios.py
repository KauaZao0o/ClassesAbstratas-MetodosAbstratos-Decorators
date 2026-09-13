"""Exercício 2: diferentes tipos de funcionários de uma empresa."""

from abc import ABC, abstractmethod


class Funcionario(ABC):
    """Classe-base para funcionários com diferentes regras salariais."""

    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base

    def exibir_dados(self) -> None:
        """Exibe os dados comuns a todos os funcionários."""
        print(f"Nome: {self.nome}")
        print(f"Salário-base: R$ {self.salario_base:.2f}")

    @abstractmethod
    def calcular_salario(self) -> float:
        """Retorna o salário final do funcionário."""


class FuncionarioCLT(Funcionario):
    """Funcionário cujo salário final inclui um bônus fixo."""

    def __init__(self, nome: str, salario_base: float, bonus: float) -> None:
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self) -> float:
        return self.salario_base + self.bonus


class FuncionarioComissionado(Funcionario):
    """Funcionário que recebe comissão percentual sobre suas vendas."""

    def __init__(
        self,
        nome: str,
        salario_base: float,
        total_vendas: float,
        percentual_comissao: float,
    ) -> None:
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_salario(self) -> float:
        comissao = self.total_vendas * self.percentual_comissao / 100
        return self.salario_base + comissao


class Estagiario(Funcionario):
    """Estagiário cujo pagamento inclui bolsa e auxílio-transporte."""

    def __init__(
        self, nome: str, salario_base: float, auxilio_transporte: float
    ) -> None:
        super().__init__(nome, salario_base)
        self.auxilio_transporte = auxilio_transporte

    def calcular_salario(self) -> float:
        return self.salario_base + self.auxilio_transporte
