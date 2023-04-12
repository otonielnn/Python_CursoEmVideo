# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço 5% de desconto.
print("Bem-vindo ao calculador de 5% de desconto.")
p = float(input("Digite o valor do produto: "))
d = p - (p * 0.05)
print(
    f"O produto é R${p:.2f}, na promoção de 5% de desconto ficará por R${d:.2f}")
