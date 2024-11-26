import requests

def get_address_by_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if "erro" not in data:
        return {
            "cep": data["cep"],
            "logradouro": data["logradouro"],
            "bairro": data["bairro"],
            "localidade": data["localidade"],
            "uf": data["uf"],
        }
    else:
        return None

cep = "79075-288"  # Substitua pelo CEP desejado
address = get_address_by_cep(cep)

if address:
    print("CEP:", address["cep"])
    print("Logradouro:", address["logradouro"])
    print("Bairro:", address["bairro"])
    print("Localidade:", address["localidade"])
    print("UF:", address["uf"])
else:
    print("CEP não encontrado.")
