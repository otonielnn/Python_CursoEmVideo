"""
    Desenvolva um programa que leia o comprimento de três retas e diga se eles podem ou não formar um triângulo.
"""
print('Seja bem vindo a análise de triângulo')
r1 = float(input('Digite o comprimento da 1º reta:'))
r2 = float(input('Digite o comprimento da 2º reta:'))
r3 = float(input('Digite o comprimento da 3º reta:'))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Os segmetos acima podem formar um triângulo')
else:
    print('Os segmetos acima NÃO podem formar um triângulo')
