import pandas as pd
import re


# Função para processar CLI_RG e separar números e emissor
def processar_rg(rg, emissor):
    if pd.isna(rg):  # Caso o RG esteja vazio ou NaN
        return "", emissor if not pd.isna(emissor) else ""

    # Remover pontos e traços
    rg_limpo = re.sub(r"[.-]", "", str(rg))

    # Separar números e o restante
    numeros = "".join(filter(str.isdigit, rg_limpo))  # Apenas números
    restante = re.sub(r"[0-9]", "", rg_limpo).strip()  # Remove números e espaços

    # Atualizar o emissor com o restante
    emissor = (str(emissor) if not pd.isna(emissor) else "").strip()
    if restante:
        emissor = f"{emissor} {restante}".strip()

    return numeros, emissor


# Carregar o arquivo CSV
arquivo_entrada = "clientes.csv"
arquivo_saida = "clientes_atualizado_rg.csv"

# Ler o arquivo CSV
df = pd.read_csv(arquivo_entrada, sep=";", encoding="utf-8")

# Garantir que as colunas necessárias existam
if "CLI_RG" in df.columns and "CLI_EMISSOR" in df.columns:
    # Aplicar a função para processar CLI_RG e CLI_EMISSOR
    df[["CLI_RG", "CLI_EMISSOR"]] = df.apply(
        lambda row: processar_rg(row["CLI_RG"], row["CLI_EMISSOR"]),
        axis=1,
        result_type="expand"
    )

    # Salvar o resultado em um novo arquivo
    df.to_csv(arquivo_saida, index=False, sep=";", encoding="utf-8")
    print(f"Arquivo processado e salvo como {arquivo_saida}")
else:
    print("As colunas CLI_RG e CLI_EMISSOR não foram encontradas no arquivo.")
