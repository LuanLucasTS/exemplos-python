import os
import datetime
from cryptography.fernet import Fernet, InvalidToken

def generate_key_with_expiration():
    # Gera uma chave de criptografia
    key = Fernet.generate_key()
    # Adicione a data de validade à chave (por exemplo, 30 dias a partir de hoje)
    expiration_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    key_with_metadata = key + b'|' + expiration_date.encode()
    return key_with_metadata

def is_key_valid(key):
    try:
        # Verifica a data de validade da chave
        expiration_date = key.split(b'|')[1].decode()
        return datetime.datetime.now() < datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
    except IndexError:
        # Se a chave não tiver uma data de validade, considere-a como válida
        return True
    except (ValueError, UnicodeDecodeError):
        # Se houver problemas ao converter a data de validade, considere a chave como inválida
        return False

# Exemplo de uso
key = generate_key_with_expiration()
print("Chave gerada:", key)

# Verifica se a chave é válida antes de usar para descriptografar
if is_key_valid(key):
    cipher_suite = Fernet(key)
    try:
        # Descriptografa os dados
        plain_text = cipher_suite.decrypt(cipher_text)
        print("Dados descriptografados:", plain_text.decode())
    except InvalidToken:
        print("Erro: A chave não é válida.")
else:
    print("Erro: A chave expirou ou é inválida.")
