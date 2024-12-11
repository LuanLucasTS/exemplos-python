import pandas as pd
import re

# Função para processar a coluna CLI_NUMERO
def processar_numero(numero, complemento):
    if pd.isna(numero):
        return "", complemento if not pd.isna(complemento) else ""  # Se não há número, não altera o complemento

    # Remove pontos e traços
    numero = re.sub(r"[.-]", "", str(numero))

    # Tentar encontrar o número principal
    match = re.match(r"(\d+)(.*)", numero)
    if match:
        primeiro_numero = match.group(1)  # O número principal
        restante = match.group(2).strip()  # O restante após o número principal

        # Adiciona o restante ao complemento
        complemento = (str(complemento) if not pd.isna(complemento) else "").strip()  # Tratar NaN como vazio
        if restante:
            complemento = f"{complemento} {restante}".strip()

        return primeiro_numero, complemento

    # Caso não haja número principal, mover tudo para o complemento
    complemento = (str(complemento) if not pd.isna(complemento) else "").strip()
    complemento = f"{complemento} {numero}".strip()

    return "", complemento

# Carregar o arquivo CSV
arquivo_entrada = "clientes.csv"
arquivo_saida = "clientes_atualizado_numero.csv"

# Ler o arquivo CSV
df = pd.read_csv(arquivo_entrada, sep=";", encoding="utf-8")

# Garantir que as colunas necessárias existam
if "CLI_NUMERO" in df.columns and "CLI_COMPLEMENTO" in df.columns:
    # Aplicar a função para processar CLI_NUMERO e CLI_COMPLEMENTO
    df[["CLI_NUMERO", "CLI_COMPLEMENTO"]] = df.apply(
        lambda row: processar_numero(row["CLI_NUMERO"], row["CLI_COMPLEMENTO"]),
        axis=1,
        result_type="expand"
    )

    # Salvar o resultado em um novo arquivo
    df.to_csv(arquivo_saida, index=False, sep=";", encoding="utf-8")
    print(f"Arquivo processado e salvo como {arquivo_saida}")
else:
    print("As colunas CLI_NUMERO e CLI_COMPLEMENTO não foram encontradas no arquivo.")
