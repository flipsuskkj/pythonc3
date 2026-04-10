'''Crie uma tupla preenchida com os 20 primeiros colocados no campeonato brasileiro de futebol,
na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.
b) Os ultimos 4 colocados da tabela.
c) uma lista com os times em ordem alfabética.
d) Em que posição está o time da chapecoense.'''

tabela = (
    "Corinthians", "Palmeiras", "Santos", "Grêmio",
    "Cruzeiro","Flamengo","Vasco","Chapecoense",
    "Atlético-MG","Botafogo", "Atlético-PR","Bahia",
    "São Paulo", "Fluminense","Sport", "Vitória",
    "Coritiba", "Avaí","Ponte Preta", "Atlético-GO"
)

chape = tabela.index('Chapecoense') + 1

print(f'Os primeiros 5 colocados são: {tabela[0:5]}')
print(f'O ultimos 4 colocados são: {tabela[16:21]}')
print(f'A tabela em ordem alfabética é: {sorted(tabela)}')
print(f'a Chapecoense está localizada na {chape}a colocação')


