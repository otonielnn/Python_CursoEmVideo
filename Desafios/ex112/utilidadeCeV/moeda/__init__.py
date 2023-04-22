def aumentar(n=0, a=0, formato=False):
    """
    -> Aumentar o  Preço (primeiro parâmetro) em % de acordo com o valor passado no segundo parâmetro.

    Args:
        n (int, optional): Preço.
        a (int, optional): Aumento.
        formato (bool, optional): mostrar com 'R$' ou não.

    Returns:
        (float): O Preço com o Aumento.
    """
    a = (a/100) * n
    n += a
    if (formato == False):
        return n
    else:
        return moeda(n)


def diminuir(n=0, r=0, formato=False):
    """
    -> reduz o Preço (primeiro parâmetro) em % de acordo com o valor passado no segundo parâmetro.

    Args:
        n (int, optional): Preço.
        r (int, optional): Redução.
        formato (bool, optional): mostrar com 'R$' ou não.

    Returns:
        float: O Preço com a Redução.
    """
    r = (r/100) * n
    n -= r
    if (formato == False):
        return n
    else:
        return moeda(n)


def dobro(n=0, formato=False):
    """
    -> O Dobro do Preço passado como primeiro parâmetro.

    Args:
        n (int, optional): Preço.
        formato (bool, optional): mostrar com 'R$' ou não.

    Returns:
        (float): O Preço multiplicado por 2 (Dobro).
    """
    n *= 2
    if (formato == False):
        return n
    else:
        return moeda(n)


def metade(n=0, formato=False):
    """
    -> A Metade do preço passado como primeiro parâmetro.

    Args:
        n (int, optional): Preço.
        formato (bool, optional): mostrar com 'R$' ou não.

    Returns:
        (float): O Preço multiplicado por 3 (Triplo).
    """
    n /= 2
    if (formato == False):
        return n
    else:
        return moeda(n)


def moeda(n=0, moeda='R$'):
    """
    -> Formatação monetária

    Args:
        n (int, optional): Preço.
        moeda (str, optional): Moeda da formatação.

    Returns:
        float: Preço com formatação monetária.
    """
    return (f'{moeda}{n:.2f}'.replace('.', ','))


def resumo(n=0, a=10, r=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de Aumento: \t{aumentar(n, a, True)}')
    print(f'{r}% de Redução: \t{diminuir(n, r, True)}')
    print('-' * 40)
