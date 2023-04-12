# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
print("Bem-vindo ao conversor de metros para centímetros e milímetros.")
m = float(input("Digite quantos metros você deseja converter: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f"A medida de {m}m corresponde a")
print(f"{km}Km")
print(f"{hm}hm")
print(f"{dam}dam")
print(f"{dm}dm")
print(f"{cm}Cm")
print(f"{mm}mm")
