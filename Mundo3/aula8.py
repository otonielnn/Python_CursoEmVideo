"""
    Tratamento de Erros e Exceções.
"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os dados digitados.')
except ZeroDivisionError:
    print('Não é possivel dividr um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
