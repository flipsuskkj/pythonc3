'''crie um programa que vai ler vários números e colocar numa lista.
Depois disso mostre:

a) quantos números foram digitados
b) a lista de valores em ordem decrescente
c) se o valor 5 foi digitado e está ou não na lista...'''
b = []
a = ''
while a != 'N':
    num = int(input('Digite um número: '))
    b.append(num)
    a = str(input('Quer continuar? [S/N] ')).upper()

print(f'Você digitou {len(b)} Números')
b.sort(reverse=True)
print(b)
if 5 in b:
    print(f'há o numero 5 na lista, mais especificamente na posição {b.index(5)}')
else:
    print('não há numero 5 na lista')