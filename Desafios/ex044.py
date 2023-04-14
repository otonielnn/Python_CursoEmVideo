"""
    Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preçoo normal e condição de pagamento
        - À vista dinheiro/cheque: 10% de desconto
        - À vista no cartão: 5% de desconto
        - em até 2x no cartão: preço normal
        - 3x ou mais: 20% de juros
"""
print('Seja Bem-vindo ao Forma de pagamento')
preço = float(input('Digite o preço do produto em R$: '))
print('''Escolha uma forma de pagamento
[ 1 ] - À vista dinheiro/cheque
[ 2 ] - À vista no cartão
[ 3 ] - Parcelado no cartão
''')
formaDePagamento = int(input('Digite a forma de pagamento: '))
if (formaDePagamento == 3):
    parcelas = int(input('Em quantas vezes deseja parcelar: '))
    if (parcelas <= 2):
        print(
            f'O produto vai custar R${preço:.2f}. Em {parcelas}x de R${preço/parcelas}')
    elif (parcelas > 2):
        juros = preço * 1.20
        print(
            f'O produto vai custar R${juros:.2f}. Em {parcelas}x de R${juros/parcelas}')
elif (formaDePagamento == 1):
    desconto = preço - (preço * 0.15)
    print(
        f'O produto vai custar R${desconto:.2f}. Com os 15% de desconto')
elif (formaDePagamento == 2):
    desconto = preço - (preço * 0.05)
    print(
        f'O produto vai custar R${desconto:.2f}. Com os 5% de desconto.')
