'''faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma unica lista composta.'''

import random as rd
import time as tm

quantidade = int(input('Quantos jogos deseja gerar: '))

jogos = []

for i in range(quantidade):
    jogo = []

    while len(jogo) < 6:
        numero = rd.randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)

    jogo.sort()
    jogos.append(jogo)

# Mostrar resultados
for i, jogo in enumerate(jogos, start=1):
    print(f"Jogo {i}: {jogo}")
    tm.sleep(1)

