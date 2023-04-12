# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
import math
print("Seja bem-vindo ao programa de mostrar a parte inteira de um número real.")
num = float(input("Digite um número real: "))
print(f"a parte inteira de {num} é {math.trunc(num)}")
