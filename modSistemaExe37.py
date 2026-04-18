# ==============================
# FUNÇÕES DE ARQUIVO
# ==============================

def arquivo_existe(nome):
    try:
        with open(nome, 'rt'):
            return True
    except FileNotFoundError:
        return False


def criar_arquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass
    except Exception as erro:
        print(f'Erro ao criar arquivo: {erro}')


def ler_arquivo(nome):
    try:
        with open(nome, 'rt') as arq:
            print('\nPESSOAS CADASTRADAS:')
            for linha in arq:
                try:
                    nome, idade = linha.strip().split(';')
                    print(f'''
===========================                    
Nome: {nome:<20}
Idade: {idade} anos
===========================''')
                except ValueError:
                    print('Linha corrompida encontrada!')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as erro:
        print(f'Erro ao ler arquivo: {erro}')


def cadastrar(nome_arq, nome, idade):
    try:
        with open(nome_arq, 'at') as arq:
            arq.write(f'{nome};{idade}\n')
    except Exception as erro:
        print(f'Erro ao cadastrar: {erro}')


# ==============================
# ENTRADA DE DADOS
# ==============================

def ler_nome():
    while True:
        nome = input('Nome: ').strip()
        if nome == '':
            print('Nome não pode ser vazio!')
        else:
            return nome


def ler_idade():
    while True:
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                print('Idade não pode ser negativa!')
            else:
                return idade
        except ValueError:
            print('Digite um número válido!')
        except KeyboardInterrupt:
            print('\nEntrada cancelada pelo usuário.')
            return 0


# ==============================
# MENU
# ==============================

def menu():
    while True:
        try:
            print('\n' + '=' * 30)
            print('MENU PRINCIPAL'.center(30))
            print('=' * 30)
            print('1 - Cadastrar pessoa')
            print('2 - Listar pessoas')
            print('3 - Sair')
            print('=' * 30)

            opc = int(input('Escolha uma opção: '))

            if opc in [1, 2, 3]:
                return opc
            else:
                print('Opção inválida!')

        except ValueError:
            print('Digite um número válido!')
        except KeyboardInterrupt:
            print('\nUsuário interrompeu o programa.')
            return 3
        finally:
            print('Obrigado por utilizar o programa!')