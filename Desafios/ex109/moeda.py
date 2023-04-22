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


def diminuir(n=0, d=0, formato=False):
    """
    -> reduz o Preço (primeiro parâmetro) em % de acordo com o valor passado no segundo parâmetro.

    Args:
        n (int, optional): Preço.
        d (int, optional): Redução.
        formato (bool, optional): mostrar com 'R$' ou não.

    Returns:
        float: O Preço com a Redução.
    """
    d = (d/100) * n
    n -= d
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
