"""
    Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
        - Abaixo de 18.5: Abaixo do peso
        - Entre 18.5 e 25: Peso ideal
        - 25 até 30: Sobrepeso
        - 30 até 40: Obesidade
        - acima de 40: Obesidade mórbida
"""
print('Seja Bem-vindo ao calculador de IMC')
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em Metros: '))
imc = peso/(altura ** 2)

if (imc < 18.5):
    print(f'O seu seu IMC é {imc:.1f}. Você está Abaixo Do Peso.')
elif (imc >= 18.5 and imc < 25):
    print(f'O seu seu IMC é {imc:.1f}. Você está no Peso Ideal.')
elif (imc >= 25 and imc < 30):
    print(f'O seu seu IMC é {imc:.1f}. Você está Sobrepeso.')
elif (imc >= 30 and imc < 40):
    print(f'O seu seu IMC é {imc:.1f}. Você está em Obesidade.')
elif (imc >= 40):
    print(f'O seu seu IMC é {imc:.1f}. Você está em Obesidade Mórbida.')
