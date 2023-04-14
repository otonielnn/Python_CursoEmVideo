"""
    Crie um programa que leia dois valores e mostre um menu na tela
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa

    seu programa deverá realizar a operação solicitada em cada caso.
"""
print('Menu de Opções')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while (opcao != 5):
    print('''Lista de opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if (opcao == 1):
        print(f'\33[32mA soma de {n1} + {n2} é {n1+n2}\033[m')
        opcao = int(input('Digite a opção desejada: '))
    elif (opcao == 2):
        print(f'\33[32mA multiplicação de {n1} * {n2} é {n1*n2}\033[m')
        opcao = int(input('Digite a opção desejada: '))
    elif (opcao == 3):
        if (n1 > n2):
            print(f'\33[32mO maior número digitado foi: {n1}\033[m')
            opcao = int(input('Digite a opção desejada: '))
        elif (n1 < n2):
            print(f'\33[32mO maior número digitado foi: {n2}\033[m')
            opcao = int(input('Digite a opção desejada: '))
        else:
            print('\33[32mOs números digitados são iguais\033[m')
            opcao = int(input('Digite a opção desejada: '))
    elif (opcao == 4):
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        opcao = int(input('Digite a opção desejada: '))
    elif (opcao == 5):
        print('\33[32m*Saindo do Programa.*')
    else:
        print('Opção Inválida. Tente novamente.')
        opcao = int(input('Digite a opção desejada: '))
