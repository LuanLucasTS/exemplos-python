import pandas as pd

# Função para mapear os valores de estado civil
def mapear_estado_civil(estado_civil):
    estado_civil = str(estado_civil).strip().upper()  # Garantir que esteja em maiúsculas e sem espaços extras
    if "CASADO" in estado_civil or "CASADA" in estado_civil:
        return "C"
    elif "DESQUITADO" in estado_civil or "DESQUITADA" in estado_civil:
        return "D"
    elif "DIVORCIADO" in estado_civil or "DIVORCIADA" in estado_civil:
        return "D"
    elif "SEPARADO" in estado_civil or "SEPARADA" in estado_civil:
        return "D"
    elif "SOLTEIRO" in estado_civil or "SOLTEIRA" in estado_civil:
        return "S"
    elif "VIÚVO" in estado_civil or "VIÚVA" in estado_civil or "VIï¿½VA" in estado_civil or "VIï¿½VO" in estado_civil:
        return "V"
    else:
        return "V"  # Retorna vazio para valores não identificados

# Carregar o arquivo CSV
arquivo_entrada = "clientes.csv"
arquivo_saida = "clientes_atualizado_estadocivil.csv"

# Ler o arquivo CSV
df = pd.read_csv(arquivo_entrada, sep=";", encoding="utf-8")

# Garantir que a coluna CLI_ESTADOCIVIL exista
if "CLI_ESTADOCIVIL" in df.columns:
    # Mapear os valores da coluna CLI_ESTADOCIVIL
    df["CLI_ESTADOCIVIL"] = df["CLI_ESTADOCIVIL"].apply(mapear_estado_civil)

    # Salvar o resultado em um novo arquivo
    df.to_csv(arquivo_saida, index=False, sep=";", encoding="utf-8")
    print(f"Arquivo processado e salvo como {arquivo_saida}")
else:
    print("A coluna CLI_ESTADOCIVIL não foi encontrada no arquivo.")
