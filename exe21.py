'''crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''

jogador = {}

jogador['nome'] = input("Nome do jogador: ")
partidas = int(input("Número de partidas: "))

gols = []

for i in range(partidas):
    gols.append(int(input(f"Gols na partida {i+1}: ")))

jogador['gols'] = gols
jogador['total'] = sum(gols)

for chave, valor in jogador.items():
    print(f"{chave}: {valor}")