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