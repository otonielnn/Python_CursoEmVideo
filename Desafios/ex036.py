"""
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da Casa, o Salário do comprador e em Quantos anos ele vai pagar.

    calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('Seja bem vindo ao banco')
salario = float(input('Digite o seu salário em R$: '))
casa = float(input('Digite o valor da casa que você deseja comprar: '))
anos = int(input('Em quantos anos você deseja pagar a casa: '))
valorMensal = casa / (anos * 12)

if (valorMensal > (salario * 0.3)):
    print(
        f'Para pagar uma casa de R${casa:.2f} em {anos} anos. a prestação será de R${valorMensal:.2f}')
    print('O seu Empréstimo foi negado.')
else:
    print(
        f'Para pagar uma casa de R${casa:.2f} em {anos} anos. a prestação será de R${valorMensal:.2f}')
    print('O seu Empréstimo foi aceito.')
