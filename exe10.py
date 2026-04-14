'''crie uma lista que vai ler vários números e colocar numa lista.

depois disso

mostre a lista completa
os pares
e os ímpares'''

a = ''
pares = []
impares = []

while a != 'N':
    num = int(input('Digite um número: '))
    a = str(input('Quer continuar? [S/N] ')).upper()
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(pares)
print(impares)
