def somar(a=0, b=0, c=0):
    s = a + b + c
    return

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f

n = int(input('digite um número: '))

print(f'O fatorial de {n} é igual a {fatorial(n)}')

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))