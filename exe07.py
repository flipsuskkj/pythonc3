'''crie um programa onde o usuario possa digitar varios valores numéricos e cadastre-os em uma lista.
 Caso o numero já exista lá dentro, ele não será adicionado.
 no final, serão todos exibiedos os valores digitados em ordem crescente.'''

a=''
b = []
while a != 'N':
    numero=int(input('digite um numero: '))
    if numero in b:
        pass
    else:
        b.append(numero)
    a = str(input('deseja continuar? [S/N]')).upper()

b.sort()
print(b)
