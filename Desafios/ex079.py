"""
    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibido todos os valores únicos digitados, em ordem crescente.
"""
lista = list()
n = 0
while True:
    n = int(input('Digite um valor: '))
    q = ''
    if (n not in lista):
        lista.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor duplicado! não vou adicionar...')

    while (q != 's' and q != 'n'):
        q = input('Deseja Continuar [S/N]? ').strip().lower()
    if (q == 'n'):
        break
print('=-' * 30)
print(f'Você digitou os valores {sorted(lista)}')
print('=-' * 30)
