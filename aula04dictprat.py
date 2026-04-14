'''locadora = [
    {'nome': 'Star Wars',
     'ano': 1977,
     'diretor': 'George lucas'},
    {'nome': 'Matrix',
     'ano': 1999,
     'diretor': 'Sla kkkkkk'},
]'''

'''pessoas = { 'nome': 'Pedro', 'sexo': 'M', 'idade': 22}'''

'''print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Felipe'
pessoas['peso'] = 53
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []

estado = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}

brasil.append(estado)
brasil.append(estado2)

#print(estado)
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    estado.clear()
'''for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')'''
for e in brasil:
    for v in e.values():
        print(v, end=' ')
        print()