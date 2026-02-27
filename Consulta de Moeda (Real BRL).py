import requests

moeda = input("Digite a moeda para consultar em relação ao BRL (ex: USD, EUR): ").upper()

try:
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
    resposta.raise_for_status()

    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave in dados:
        info = dados[chave]

        print("Valor atual:", info["bid"])
        print("Máxima do dia:", info["high"])
        print("Mínima do dia:", info["low"])
        print("Última atualização:", info["create_date"])
    else:
        print("Moeda não encontrada.")

except requests.exceptions.RequestException:
    print("Erro na requisição.")