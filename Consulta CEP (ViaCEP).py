import requests

cep = input("Digite o CEP (somente números): ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    resposta.raise_for_status()

    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Logradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except requests.exceptions.RequestException:
    print("Erro na requisição.")