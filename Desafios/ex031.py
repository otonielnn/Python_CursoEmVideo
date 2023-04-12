"""
    Desenvolva um programa que pergunte a distância de uma viagem em Km. calcule o preço da pasagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
print('Seja bem-vindo ao custo de viagem')
km = int(input("Digite quantos Km de distância é sua viagem: "))
if (km <= 200):
    print(f'A sua viagem de {km}Km vai custar: R${km*0.50:.2f}')
else:
    print(f'A sua viagem de {km}Km vai custar: R${km * 0.45:.2f}')
