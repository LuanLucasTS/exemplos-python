import pandas as pd
import re

# Caminho do arquivo CSV
file_path = "clientes.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se as colunas CLI_NUMERO e CLI_COMPLEMENTO existem
numero_col = "CLI_NUMERO"
complemento_col = "CLI_COMPLEMENTO"

if numero_col not in df.columns:
    raise ValueError(f"A coluna '{numero_col}' não foi encontrada no arquivo.")

# Garantir que a coluna CLI_COMPLEMENTO exista
if complemento_col not in df.columns:
    df[complemento_col] = ""

# Função para separar números e não números
def processar_numero(valor):
    if isinstance(valor, str):
        # Extrair apenas números
        numeros = re.findall(r"\d+", valor)
        numeros = "".join(numeros) if numeros else ""
        # Extrair o restante (não numérico)
        nao_numerico = re.sub(r"\d+", "", valor).strip()
        return numeros, nao_numerico
    return valor, ""  # Retorna vazio para não numéricos caso valor não seja string

# Aplicar a função para processar CLI_NUMERO
df[numero_col], complementos = zip(*df[numero_col].apply(processar_numero))

# Adicionar os complementos existentes na coluna CLI_COMPLEMENTO
df[complemento_col] = df[complemento_col].fillna("") + " " + pd.Series(complementos)
df[complemento_col] = df[complemento_col].str.strip()  # Remover espaços extras

# Remover pontos que estão sozinhos na coluna CLI_COMPLEMENTO
df[complemento_col] = df[complemento_col].apply(lambda x: "" if x.strip() == "." else x)

# Salvar o arquivo atualizado
output_file = "clientes_atualizado_numeros.csv"
df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo atualizado salvo em: {output_file}")
