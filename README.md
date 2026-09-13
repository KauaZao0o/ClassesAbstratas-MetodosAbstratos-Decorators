# Classes Abstratas, Métodos Abstratos e Decorators

Solução em Python para três exercícios sobre herança, abstração e decorators.

## Exercícios

1. **Sistema de pagamentos:** classe abstrata `Pagamento` e implementações para PIX
   e cartão.
2. **Funcionários:** classe abstrata `Funcionario`, funcionários CLT e
   comissionados, além do desafio da classe `Estagiario`.
3. **Registro de execução:** decorator compatível com diferentes argumentos por
   meio de `*args` e `**kwargs`, incluindo o desafio de mostrar o nome da função.

## Como executar

É necessário ter Python 3.9 ou mais recente instalado.

```bash
python main.py
```

Para executar os testes automatizados:

```bash
python -m unittest -v
```

## Organização

- `pagamento.py`: solução do exercício 1.
- `funcionarios.py`: solução do exercício 2 e seu desafio.
- `decorators.py`: solução do exercício 3 e seu desafio.
- `main.py`: cria os objetos e demonstra todos os métodos.
- `test_exercicios.py`: testes automatizados.

## Por que `Pagamento` não pode ser instanciada diretamente?

`Pagamento` herda de `ABC` e possui `processar_pagamento()` marcado com
`@abstractmethod`. Por isso, tentar executar `Pagamento(100)` gera um `TypeError`.
A classe abstrata define o contrato comum, mas uma subclasse concreta precisa
implementar o método abstrato antes que um objeto possa ser criado.
