'''Crie um código em python que teste se o site pudim está acessível pelo computador usado'''

from requests import get, exceptions, RequestException


def verificar_site(url):
    try:
        resposta = get(url, timeout=5)

        if resposta.status_code == 200:
            return True, "Site acessível"

        else:
            return False, f"Site indisponível (Status: {resposta.status_code})"

    except exceptions.RequestException as e:
        return False, f"Erro ao acessar: {e}"

    finally:
        print('Obrigado por utilizar esse programa!')


url = "https://pudim.com.br"
status, mensagem = verificar_site(url)
print(f"{url}: {mensagem}")
