import pandas as pd
import re

# Caminho do arquivo CSV
file_path = "clientes.csv"

# Tentativa de carregar o arquivo com tratamento de erros
try:
    df = pd.read_csv(file_path, sep=";", encoding="utf-8", on_bad_lines="skip")
except UnicodeDecodeError:
    # Tenta com outra codificação, caso a primeira falhe
    df = pd.read_csv(file_path, sep=";", encoding="latin1", on_bad_lines="skip")

# Verificar se a coluna 'CLI_INSCRICAOMUNICIPAL' existe
column_name = "CLI_INSCRICAOMUNICIPAL"
if column_name not in df.columns:
    raise ValueError(f"A coluna '{column_name}' não foi encontrada no arquivo.")

# Função para limpar os valores
def clean_inscricao(value):
    if isinstance(value, str) and value.upper() == "ISENTO":
        return "ISENTO"
    if isinstance(value, str):
        return re.sub(r"[^\d]", "", value)
    return value

# Aplicar a limpeza na coluna F
df[column_name] = df[column_name].apply(clean_inscricao)

# Salvar o resultado em um novo arquivo com separador ";"
output_file_path = "clientes_processado.csv"
df.to_csv(output_file_path, index=False, encoding="utf-8", sep=";")

print(f"Arquivo processado salvo em: {output_file_path}")
