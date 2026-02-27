# Função para calcular gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Testando a função
valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

resultado = calcular_gorjeta(valor, porcentagem)

print(f"Gorjeta: R$ {resultado:.2f}")