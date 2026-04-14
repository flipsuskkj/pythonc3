'''crie um programa onde o usuaria possa digitar sete valores numéricos e cadastre os em uma lista unica
que mantenha separados os valores pares e impares.
No final mostre os valores pares e impares em ordem crescente.'''

par=list()
impar=list()
parimpar=list()
for i in range(0,7):
    b=int(input('Digite um valor: '))
    if b%2==0:
        par.append(b)
    else:
        impar.append(b)

parimpar.append(par)
parimpar.append(impar)

print(parimpar)