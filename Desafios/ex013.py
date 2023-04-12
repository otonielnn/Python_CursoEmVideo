# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print("Bem-vindo ao calculador de 15% de aumento")
s = float(input("Digite o seu salário atual: "))
a = s + (s * 0.15)
print(f"O seu salário de R${s:.2f}, com o aumento de 15% ficará R%{a:.2f}")
