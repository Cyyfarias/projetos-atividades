import pandas as pd

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    df = pd.read_csv(arquivo)

    media = df["tempo_execucao"].mean()
    desvio = df["tempo_execucao"].std()

    print(f"Média: {media:.2f}")
    print(f"Desvio padrão: {desvio:.2f}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except KeyError:
    print("Erro: coluna 'tempo_execucao' não encontrada.")
except Exception as e:
    print("Erro na leitura do arquivo:", e)