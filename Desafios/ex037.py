"""
    Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
        - 1 para binário
        - 2 para octal
        - 3 para hexadecimal
"""
print('Seja Bem-vindo ao conversor de base númerica')
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases númericas para conversão: 
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] convertr para Hexadecimal''')
opcao = int(input('Digite sua opção: '))

if (opcao == 1):
    print(f'{n} convertido para Binário é igual a {bin(n)[2:]}')
elif (opcao == 2):
    print(f'{n} convertido para Octal é igual a {oct(n)[2:]}')
elif (opcao == 3):
    print(f'{n} convertido para Hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção Inválida, tente novamente.')
