'''crie umprograma onde o usuario pode digitar cinco valores e cadastre-os numa lista
já na posição correta de inserção(sem usar o sort)'''

lista = []

for i in range(5):
    valor = int(input(f"Digite o {i + 1}º valor: "))

    if i == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1

print("Lista ordenada:", lista)