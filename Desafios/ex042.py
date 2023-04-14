"""
    Refaça o Desafio 035 dos Triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
        - Equilátero: todos laods iguais
        - Isósceles: dois lados iguais
        - Escaleno: Todos lados diferentes
"""
print('Seja bem vindo a análise de triângulo')
r1 = float(input('Digite o comprimento da 1º reta: '))
r2 = float(input('Digite o comprimento da 2º reta: '))
r3 = float(input('Digite o comprimento da 3º reta: '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    if (r1 == r2 and r1 == r3 and r2 == r3):
        print('Os segmetos acima podem formar um triângulo Equilátero.')
    elif (r1 != r2 and r1 != r3 and r2 != r3):
        print('Os segmetos acima podem formar um triângulo Escaleno.')
    elif (r1 == r2 or r1 == r3 or r2 == r3):
        print('Os segmetos acima podem formar um triângulo Isósceles.')
else:
    print('Os segmetos acima NÃO podem formar um triângulo.')
