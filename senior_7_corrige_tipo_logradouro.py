import pandas as pd

# Caminho do arquivo CSV
file_path = "clientes_logradouros_limpos.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se a coluna TIPO_LOGRADOURO existe
tipo_col = "TIPO_LOGRADOURO"

if tipo_col not in df.columns:
    raise ValueError(f"A coluna '{tipo_col}' não foi encontrada no arquivo.")

# Lista de tipos válidos
tipos_validos = {"R", "AV", "TV"}

# Corrigir os valores na coluna TIPO_LOGRADOURO
df[tipo_col] = df[tipo_col].apply(lambda x: x if x in tipos_validos else "R")

# Salvar o arquivo corrigido
output_file = "clientes_tipo_logradouro_corrigido.csv"
df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo corrigido salvo em: {output_file}")
