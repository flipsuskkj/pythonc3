'''Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem das pessoas mais pesadas.
C) Uma listagem das pessoas mais leves.'''


a=''
b=list() #lista add
c=list() #lista comp
pesados=list()
leves=list()
while a != 'N':
    b.append(str(input('Nome: ')))
    b.append(float(input('Peso: ')))
    c.append(b[:])
    b.clear()
    a = str(input('Quer continuar? [S/N] ')).upper()

for p in c:
    if p[1] > 80:
        pesados.append(p)

    elif p[1] < 80:
        leves.append(p)

print(f'{len(c)} pessoas foram cadastradas.')
print(f'{len(pesados)} pessoas pesadas cadastradas. {pesados}')
print(f'{len(leves)} pessoas leves cadastradas. {leves}')


