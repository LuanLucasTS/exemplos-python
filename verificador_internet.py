import urllib.request

def verificar_conexao(url='http://www.google.com'):
    try:
        urllib.request.urlopen(url, timeout=5)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if verificar_conexao():
        print("Conexão com a internet ativa.")
    else:
        print("Sem conexão com a internet.")
