"""
    Funções
        - Interactive Help
        - Docstrings
        - Argumentos
        - Escopo de variáveis
        - Retorno de resultados
"""
"""
help(print) # explica funções/metodos da linguagem
print(input.__doc__) # outra forma.
"""


# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.

#     Args:
#         i (int): início da contagem
#         f (int): fim da contagem
#         p (int): passo da contagem
#     """
#     c = i
#     while c <= f:
#         print(f'{c} ', end='')
#         c += p
#     print('Fim!')


# help(contador)

# def somar(a=0, b=0, c=0):
#     """
#     -> Faz soma de três valores e mostra o resultado na tela.

#     Args:
#         a (float): o primeiro valor
#         b (float): o segundo valor
#         c (float): o terceiro valor
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')


# somar(3, 2)

"""
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
# print(f'No programa principal, x vale {x}') //  x é uma variável local da função
"""


"""
def funcao():
    n1
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {1}')
"""


"""
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2)
r2 = somar(2, 2)
r3 = somar(6)
print(f'As somas valem {r1}, {r2} e {r3}')
"""


"""
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
"""


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
