# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27
print("Bem-vindo ao conversor de R$ para US$. (cotação US$1,00 = R$3,27)")
r = float(input("Digite quantos R$ você tem: "))
d = r / 3.27
print(f"Com R${r} você pode comprar US${d:.2f}")
