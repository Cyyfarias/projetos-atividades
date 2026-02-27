# Programa de desconto

preco = float(input("Digite o preço do produto: R$ "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco * (porcentagem / 100)
preco_final = preco - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")