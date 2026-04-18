'''Reescreva a função leiaint() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um número de tipo invalido,
Aproveite e crie a função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('\n Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except KeyboardInterrupt:
            print('\n Entrada de dados interrompida pelo usuário.')
            return 0.0
        else:
            return n

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')

print(f'Você digitou o inteiro {inteiro} e o real {real:.2f}')