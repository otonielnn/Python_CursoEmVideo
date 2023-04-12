# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangentxe desse ângulo.
import math
print("Seja Bem-vindo ao programa de seno, cosseno e tangente")
angulo = float(input("Digite o valor do ângulo: "))
print(f"O seno do ângulo de {angulo}º é {math.sin(math.radians(angulo)):.2f}")
print(
    f"O cosseno do ângulo de {angulo}º é {math.cos(math.radians(angulo)):.2f}")
print(
    f"O tangente do ângulo de {angulo}º é {math.tan(math.radians(angulo)):.2f}")
