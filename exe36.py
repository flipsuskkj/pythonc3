'''Crie um código em python que teste se o site pudim está acessível pelo computador usado'''

from requests import get, exceptions, RequestException

def verificar_site(url):
    try:
        # Envia uma solicitação GET, com um tempo limite (timeout) de 5 segundos
        resposta = get(url, timeout=5)
        # Verifica se o código de status é 200 (OK)
        if resposta.status_code == 200:
            return True, "Site acessível"
        else:
            return False, f"Site indisponível (Status: {resposta.status_code})"
    except exceptions.RequestException as e:
        # Captura erros de conexão, DNS, timeout, etc.
        return False, f"Erro ao acessar: {e}"
    finally:
        print('Obrigado por utilizar esse programa!')
# Exemplo de uso
url = "https://pudim.com.br"
status, mensagem = verificar_site(url)
print(f"{url}: {mensagem}")
