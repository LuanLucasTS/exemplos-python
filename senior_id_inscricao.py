import pandas as pd

# Caminho do arquivo CSV
file_path = "clientes.csv"

# Carregar o arquivo processado
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se a coluna 'ID_INSCRIÇÃO' existe
column_name = "ID_INSCRICAO"
if column_name not in df.columns:
    raise ValueError(f"A coluna '{column_name}' não foi encontrada no arquivo.")

# Substituir valores na coluna
df[column_name] = df[column_name].replace({"J": 1, "F": 2})

# Salvar o resultado em um novo arquivo
output_file_path = "clientes_processado.csv"
df.to_csv(output_file_path, index=False, encoding="utf-8", sep=";")

print(f"Arquivo final salvo em: {output_file_path}")
