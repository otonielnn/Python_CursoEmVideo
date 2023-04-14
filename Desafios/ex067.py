"""
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while (True):
    n = int(input('Digite o número que deseja ver a tabuada: '))
    if (n > 0):
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')
    else:
        print('*Finalizando o programa*')
        break
