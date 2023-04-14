"""
    Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pause de 1 segundo entre eles.
"""
import time
print('*Começando a contagem Regressiva dos fogos de Artificio*')
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print('Fim')
