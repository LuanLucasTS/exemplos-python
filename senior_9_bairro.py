import pandas as pd

# Caminho do arquivo CSV
file_path = "clientes.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se a coluna CLI_BAIRRO existe
bairro_col = "CLI_BAIRRO"

if bairro_col not in df.columns:
    raise ValueError(f"A coluna '{bairro_col}' não foi encontrada no arquivo.")

# Remover a palavra "BAIRRO" do início das células
df[bairro_col] = df[bairro_col].str.replace(r"^BAIRRO\s*", "", case=False, regex=True)

# Salvar o arquivo atualizado
output_file = "clientes_atualizado_bairro.csv"
df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo atualizado salvo em: {output_file}")
