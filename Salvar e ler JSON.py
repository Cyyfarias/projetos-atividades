import json

arquivo = "dados.json"

dados = {
    "nome": "Juliana",
    "idade": 28,
    "cidade": "Curitiba"
}

# Salvando no JSON
try:
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

    print("Dados salvos com sucesso!")

except Exception:
    print("Erro ao salvar o arquivo.")

# Lendo o JSON
try:
    with open(arquivo, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)

    print("Dados lidos do arquivo:")
    print("Nome:", dados_lidos["nome"])
    print("Idade:", dados_lidos["idade"])
    print("Cidade:", dados_lidos["cidade"])

except FileNotFoundError:
    print("Arquivo JSON não encontrado.")
except Exception:
    print("Erro ao ler o arquivo.")