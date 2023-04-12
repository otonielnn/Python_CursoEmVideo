# Escreva um programa que pergunte a quantidade de Km percorridas por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por Km rodado
print("Seja bem-vindo ao calculador de aluguel de carro.")
d = int(input("Digite quantos dias ficou com carro: "))
km = float(input("Digite quantos Km você percorreu com o carro: "))
print(
    f"O valor a ser pago por {d} dias e ter percorrido {km}Km é R${(d * 60) + (km * 0.15):.2f} .")
