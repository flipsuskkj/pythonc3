
def aumentar(valor, percentual, formatar=False):
    resultado = valor + (valor * percentual / 100)
    return moeda(resultado) if formatar else resultado


def diminuir(valor, percentual, formatar=False):
    resultado = valor - (valor * percentual / 100)
    return moeda(resultado) if formatar else resultado


def dobro(valor, formatar=False):
    resultado = valor * 2
    return moeda(resultado) if formatar else resultado


def metade(valor, formatar=False):
    resultado = valor / 2
    return moeda(resultado) if formatar else resultado


def moeda(valor, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')


def resumo(valor, aumento=10, reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 30)