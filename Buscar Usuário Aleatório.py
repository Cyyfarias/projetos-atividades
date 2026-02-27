import requests

try:
    resposta = requests.get("https://randomuser.me/api/")
    resposta.raise_for_status()

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print("Falha ao conectar à API.")