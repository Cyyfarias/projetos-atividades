arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")

pessoas = [
    {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Mariana", "idade": 22, "cidade": "Belo Horizonte"}
]

try:
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("Nome\tIdade\tCidade\n")
        f.write("-" * 30 + "\n")

        for pessoa in pessoas:
            f.write(f"{pessoa['nome']}\t{pessoa['idade']}\t{pessoa['cidade']}\n")

    print("Arquivo salvo com sucesso!")

except Exception:
    print("Erro ao salvar o arquivo.")