def aumentar(n=0, a=0):
    a = (a/100) * n
    n += a
    return n


def diminuir(n=0, a=0):
    a = (a/100) * n
    n -= a
    return n


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(n=0, moeda='R$'):
    return (f'{moeda}{n:.2f}'.replace('.', ','))
