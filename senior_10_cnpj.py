import pandas as pd
import re

# Caminho do arquivo CSV
file_path = "clientes.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se as colunas CLI_TIPO e CLI_CNPJ existem
tipo_col = "CLI_TIPO"
cnpj_col = "CLI_CNPJ"

if tipo_col not in df.columns or cnpj_col not in df.columns:
    raise ValueError(f"As colunas '{tipo_col}' ou '{cnpj_col}' não foram encontradas no arquivo.")

# Função para validar e aplicar as alterações no CNPJ
def processar_cnpj(tipo, cnpj):
    if tipo == "F":
        return ""  # Apagar o conteúdo do CNPJ se o tipo for "F"
    elif tipo == "J":
        # Remover caracteres não numéricos
        numeros = re.sub(r"\D", "", str(cnpj))
        if len(numeros) == 13:  # Se o CNPJ tem 13 dígitos, adicionar um 0 no início
            numeros = "0" + numeros
        if len(numeros) == 14:  # Verificar se agora tem 14 dígitos
            return f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"
        else:
            return cnpj  # Retornar o valor original se não for um CNPJ válido
    else:
        return cnpj  # Manter o valor original para outros casos

# Aplicar a função na coluna CLI_CNPJ
df[cnpj_col] = df.apply(lambda row: processar_cnpj(row[tipo_col], row[cnpj_col]), axis=1)

# Salvar o arquivo atualizado
output_file = "clientes_atualizado_cnpj.csv"
df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo atualizado salvo em: {output_file}")
