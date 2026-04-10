comidas = ('hamburguer', 'suco', 'pizza', 'pudim')
for c in comidas:
    print(c)
print(len(comidas))
for comida in comidas:
    print(f'Eu vou comer {comida}')

for cont in range(0,len(comidas)):
    print(f'Eu vou comer {comidas[cont]} na posição {cont}')

for pos, comida in enumerate(comidas):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(comidas))

print('comi pra caramba')
#tuplas são IMUTÁVEIS porra

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
#out 2
print(c.index(5))
#out 1
#a+b != b+a

pessoa = ('felipe', 17, 'M', 56.76, True)
print(pessoa)
print(pessoa[0])