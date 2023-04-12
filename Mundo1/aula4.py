"""
    biblioteca Math
        ceil - arredonda para cima
        floor -arredonda para baixo
        trunc - deixa apenas a parte inteira
        pow - power (potência)
        sqrt - square root (raiz quadrada)
        factorial - fatorial

    biblioteca random
        gera número aleatórios
"""
import math
num = float(input("Digite um número: "))
raiz = math.sqrt(num)
potencia = math.pow(num, 2)
fatorial = math.factorial(int(num))
cima = math.ceil(num)
baixo = math.floor(num)
inteiro = math.trunc(num)
print(f"a raiz quadrada é {raiz}")
print(f"a potência é {potencia}")
print(f"o fatorial é {fatorial}")
print(f"arredondando para cima {cima}")
print(f"arredondando para baixo {baixo}")
print(f"A parte inteira {inteiro}")
