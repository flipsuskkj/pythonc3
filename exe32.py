'''crie uma função leiaint(), que vai funcionar de forma semelhante à função input
do python, só que fazendo a validação para aceitar apenas um valor numérico

ex:
n = leiaint('Digite um N: )'''

def leiaint(msg):
    n = input(msg)
    try:
        int(n)
        print('\033[32mTrue\033[m')   # verde
        return True
    except (ValueError, TypeError):
        print('\033[31mFalse\033[m')  # vermelho
        return False


# uso
resultado = leiaint('Digite algo: ')