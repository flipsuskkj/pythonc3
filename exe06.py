'''faça um programa que leia 5 valores numéricos e guarde numa lista
no final mostre qual foi o maior e qual foi o menor valor digitado e suas respectivas posições na lista.'''

a = []
for i in range(5):
    a.append(int(input('Digite um valor: ')))

print(f'O maior valor digitado foi {max(a)} na posição {a.index(max(a))}')
print(f'O menor valor digitado foi {min(a)} na posição {a.index(min(a))}')