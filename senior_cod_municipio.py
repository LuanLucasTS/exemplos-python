import pandas as pd

# Caminho do arquivo principal e do arquivo de referência
clientes_file = "clientes.csv"
ibge_file = "cod_municipio.csv"

# Carregar o arquivo principal e o arquivo de referência
clientes_df = pd.read_csv(clientes_file, sep=";", encoding="utf-8")
ibge_df = pd.read_csv(ibge_file, sep=";", encoding="utf-8")

# Garantir que os nomes das cidades estejam na mesma capitalização
clientes_df["CLI_CIDADE"] = clientes_df["CLI_CIDADE"].str.strip().str.upper()
ibge_df["cidade"] = ibge_df["cidade"].str.strip().str.upper()

# Mapear os códigos IBGE para a coluna CLI_CIDADE
cidade_to_codigo = dict(zip(ibge_df["cidade"], ibge_df["codigo_ibge"]))
clientes_df["COD_MUNICIPIO"] = clientes_df["CLI_CIDADE"].map(cidade_to_codigo)

# Remover valores NaN e converter para inteiro
clientes_df["COD_MUNICIPIO"] = clientes_df["COD_MUNICIPIO"].fillna(0).astype(int)

# Salvar o arquivo atualizado
output_file = "clientes_com_codigos.csv"
clientes_df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

print(f"Arquivo atualizado salvo em: {output_file}")
