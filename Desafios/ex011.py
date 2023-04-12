# Faça um programa que leia a largura e a altura de uma parede em metros, cacule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
print("Bem-vindo ao caculador de área")
l = float(input("Digite a largura da parede em Metros: "))
a = float(input("Digite a altura da parede em Metros: "))
area = l * a
tinta = area / 2
print(f"Sua parede tem {l}m de largura e {a}m de altura.")
print(
    f"A área da sua parede é {area}m². Sendo necessário {tinta} litros de tinta para pintar a parede toda.")
