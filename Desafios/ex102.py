"""
    Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
"""


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    Args:
        n (int): O número a ser calculado.
        show (bool, optional): Mostrar ou não a conta.

    Returns:
        int: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if (i > 1):
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(fatorial(5))
print(fatorial(5, show=True))
help(fatorial)
