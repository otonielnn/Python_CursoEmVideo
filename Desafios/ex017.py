# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
print("Seja Bem-vindo ao calculador de hipotenusa")
oposto = float(input("digite o comprimento do cateto oposto: "))
adjacente = float(input("digite o comprimento do cateto adjacente: "))
print(f"Cateto oposto = {oposto}. Cateto adjacente = {adjacente}.")
print(f"A hipotenusa será {math.hypot(oposto, adjacente):.2f}")
