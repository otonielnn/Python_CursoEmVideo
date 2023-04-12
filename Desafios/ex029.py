"""
    Escreva um programa que leia a velocidade de um carro.
    se  ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada KM acima do limite
"""
print('Seja Bem-vindo ao radar')
velocidade = int(input('Qual a sua velocidade atual em Km/h: '))
if (velocidade > 80):
    print('Você ultrapassou o limite de 80Km/h e será multado em R$7,00 por Km excedido')
    print(f'total a pagar: R${(velocidade - 80)*7:.2f}')
else:
    print('Você está dentro do limite de velocidade.')
