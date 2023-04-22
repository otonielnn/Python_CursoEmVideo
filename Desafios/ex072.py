"""
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('digite um número entre 0 e 20: '))
    q = ''
    if (0 <= n <= 20):
        print(f'Você digitou o número {numeros[n]}')
        while (q != 's' and q != 'n'):
            q = input('Quer continuar [S/N]? ').strip().lower()
        if (q == 'n'):
            break
    else:
        print('Tente Novamente. ')
