# Classificador de Pares e Ímpares

quantidade = int(input("Quantos números você deseja digitar? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i+1}: "))
    
    if numero % 2 == 0:
        print("Par")
        pares += 1
    else:
        print("Ímpar")
        impares += 1

print("Total de pares:", pares)
print("Total de ímpares:", impares)