'''teste = list()
teste.append('Felipe')
teste.append(17)
povo = list()
povo.append(teste)
teste[0] = 'Laura'
teste[1] = 16
povo.append(teste[:])
print(povo)'''

'''povo = [['Felipe', 17], ['Laura', 16], ['Kauan', 12], ['Elaine', 38], ['Felippe', 52]]
for p in povo:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

povo = list()
dado = list()
totmai = totmen = 0
for c in range(1, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    povo.append(dado[:])
    dado.clear()

for p in povo:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'{totmai} maiores de idade.')
print(f'{totmen} menores de idade.')
print(f'')

