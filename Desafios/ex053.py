"""
    Crie um programa que leia uma frase e diga se ela é um palindromo, desconsiderando os espaços
"""
print('Análise de Palíndromo')
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
if (inverso == junto):
    print('Temos um Palíndromo')
else:
    print('A Frase digitada não é um Palíndromo')
