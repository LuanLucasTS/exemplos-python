import pandas as pd
import re

# Caminho do arquivo CSV
file_path = "clientes.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Verificar se a coluna CLI_LOGRADOURO existe
logradouro_col = "CLI_LOGRADOURO"
tipo_col = "TIPO_LOGRADOURO"

if logradouro_col not in df.columns:
    raise ValueError(f"A coluna '{logradouro_col}' não foi encontrada no arquivo.")

# Função para extrair o tipo de logradouro e o restante do endereço, incluindo casos com ponto colado
def separar_logradouro(endereco):
    if isinstance(endereco, str):
        # Remove espaços no início e aplica o regex
        endereco = endereco.strip()
        # Atualizado para lidar com tipos colados com ponto
        match = re.match(r"^(\S+?)(?:\.|\s)+(.*)", endereco)
        if match:
            return match.group(1), match.group(2)
    return "", endereco  # Retorna vazio para TIPO_LOGRADOURO se não encontrar o padrão

# Aplicar a função e criar as novas colunas
df[tipo_col], df[logradouro_col] = zip(*df[logradouro_col].apply(separar_logradouro))

# Salvar o arquivo atualizado
output_file = "clientes_atualizado.csv"
df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo corrigido salvo em: {output_file}")
