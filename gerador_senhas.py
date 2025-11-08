import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha: "))
    print("Senha gerada:", gerar_senha(tamanho))
