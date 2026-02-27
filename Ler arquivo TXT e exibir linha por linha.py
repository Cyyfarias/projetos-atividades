arquivo = input("Digite o nome do arquivo para ler: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception:
    print("Erro ao ler o arquivo.")