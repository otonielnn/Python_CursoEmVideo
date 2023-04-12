"""
    Ordem de precedência
    1 - ()
    2 - **
    3 - *, /, //, %
    4 - +, -
"""
n1 = int(input("Digite 1º número: "))
n2 = int(input("Digite 2º número: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f"A soma é {s}, o produto é {m} e a divisão é {d:.3}")
print(f"Divisão inteira {di} e potência {e}")
