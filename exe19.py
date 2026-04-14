'''crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. no final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o mairo número no dado.'''

import random

jogadores = {}

for i in range(1, 5):
    jogadores[f'Jogador {i}'] = random.randint(1, 6)

for jogador, valor in jogadores.items():
    print(f"{jogador} tirou {valor}")

ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

print("\n--- Ranking ---")
for posicao, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{posicao}º lugar: {jogador} com {valor}")