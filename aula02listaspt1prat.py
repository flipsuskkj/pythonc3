
'''
num[2] = 999
num.append(289)
num.sort()
num.sort(reverse=True)
num.insert(2,0)
print(num)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
if 19 in num:
    num.remove(0)
else:
    print('não tem numero 0190 em num')
'''
#num = [1,2,3,4,5,6,7,8,9]

'''for c, valor in enumerate(num):
    print(valor)
    print(f'na posição {c} achei o numero {valor}!!!')
print('FIM DA LINHA!!!')

l = list()
for cont in range(0,10):
    l.append(int(input('Digite um numero: ')))'''

a = [1,2,3,4]
b = a[:] #cópia, não tem ligação, diferente de a = b
b[2] = 8   #com as listas igualadas, os valores das duas são iguais, ou seja (out a: 1,2,8,4. out b: 1,2,8,4)
a.append(3)
print(a)
print(b)