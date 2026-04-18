def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.replace('.', '', 1).isdigit():
            return float(entrada)
        else:
            print(f'ERRO: "{entrada}" é um preço inválido!')