'''aprimore o desfio 93 (aprovfeitamento do jogador)
para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamenti de cada jogador.
'''

time = []

while True:
    jogador = {}
    jogador['nome'] = input("Nome do jogador: ")
    partidas = int(input("Número de partidas: "))

    gols = []
    for i in range(partidas):
        gols.append(int(input(f"Gols na partida {i + 1}: ")))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    time.append(jogador)

    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print("\n--- Tabela de jogadores ---")
print("cod  nome           gols           total")
print("-" * 45)

for i, j in enumerate(time):
    print(f"{i:<4} {j['nome']:<14} {str(j['gols']):<15} {j['total']}")

while True:
    busca = int(input("\nMostrar dados de qual jogador? (999 para parar): "))

    if busca == 999:
        break

    if busca >= len(time):
        print("Jogador não existe.")
    else:
        print(f"\n-- Levantamento do jogador {time[busca]['nome']} --")
        for i, g in enumerate(time[busca]['gols']):
            print(f"No jogo {i + 1} fez {g} gols.")