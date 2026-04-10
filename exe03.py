'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os numa tupla. no final, mostre:
a) quantas vezes apareceu o valor 9
b)Em que posição foi digitado o primeiro valor 3
c)quais foram os numeros pares.'''


a = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
pares = [num for num in range(1, 10) if num % 2 == 0]

print(a)
print(f'O numero 9 foi digitado {a.count(9)} vezes' if a[0] ==9 or a[1] ==9or a[2] ==9 or a[3] == 9 else 'Sem nenhum numero 9 atribuido a tupla')
print(f'O numero 3 apareceu primeiro na posição {a.index(3)}, ou {a.index(3)+1} pros não pythonianos'if a[0] ==3 or a[1] ==3 or a[2] ==3 or a[3] == 3 else 'Nenhum numero 3' )
print(pares)