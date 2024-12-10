import pandas as pd
import re

# Caminho do arquivo CSV
file_path = "clientes_atualizado.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se a coluna CLI_LOGRADOURO existe
logradouro_col = "CLI_LOGRADOURO"

if logradouro_col not in df.columns:
    raise ValueError(f"A coluna '{logradouro_col}' não foi encontrada no arquivo.")

# Função para remover os prefixos indesejados
def limpar_logradouro(endereco):
    if isinstance(endereco, str):
        # Regex para substituir os prefixos mencionados
        endereco = re.sub(r"^(R |R\.|R:|RUA|TRAV\.|AV\.|AV )\s*", "", endereco, flags=re.IGNORECASE)
    return endereco

# Aplicar a função para limpar a coluna CLI_LOGRADOURO
df[logradouro_col] = df[logradouro_col].apply(limpar_logradouro)

# Salvar o arquivo atualizado
output_file = "clientes_logradouros_limpos.csv"
df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo atualizado salvo em: {output_file}")
