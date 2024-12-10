import pandas as pd
import re


# Função para aplicar a máscara no CPF
def aplicar_mascara(cpf):
    # Remove qualquer caractere não numérico
    cpf = re.sub(r"\D", "", str(cpf))

    # Verifica se o CPF tem 11 dígitos (caso contrário, retorna vazio)
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return ""  # Retorna vazio se não tiver 11 dígitos


# Caminho do arquivo CSV
file_path = "clientes.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se as colunas CLI_TIPO e CLI_CPF existem
tipo_col = "CLI_TIPO"
cpf_col = "CLI_CPF"

if tipo_col not in df.columns or cpf_col not in df.columns:
    raise ValueError(f"As colunas '{tipo_col}' ou '{cpf_col}' não foram encontradas no arquivo.")


# Função para processar o CPF de acordo com a regra
def processar_cpf(tipo, cpf):
    if tipo == "J":
        return ""  # Apagar o conteúdo do CPF se o tipo for "J"
    return aplicar_mascara(cpf)  # Aplicar a máscara se o tipo for "F"


# Aplicar a função na coluna CLI_CPF
df[cpf_col] = df.apply(lambda row: processar_cpf(row[tipo_col], row[cpf_col]), axis=1)

# Salvar o arquivo atualizado
output_file = "clientes_atualizado_cpf.csv"
df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo atualizado salvo em: {output_file}")
