'''Crie um pequeno sistema modularizado que permita cadastrar pessoas
pelo seu nome e idade em um arquivo de texto simples>

O sistema só vai ter 2 opções:
Cadastrar uma nova pessoa e
Listar todas as pessoas cadastradas.'''

import modSistemaExe37 as pessoas #nékkkkkkkk

ARQ = 'pessoas.txt'

if not pessoas.arquivo_existe(ARQ):
    pessoas.criar_arquivo(ARQ)

while True:
    opc = pessoas.menu()

    if opc == 1:
        nome = pessoas.ler_nome()
        idade = pessoas.ler_idade()
        pessoas.cadastrar(ARQ, nome, idade)

    elif opc == 2:
        pessoas.ler_arquivo(ARQ)

    elif opc == 3:
        print('Saindo... até mais!')
        break