# Verificador de Senha

senha = input("Digite sua senha: ")

tem_numero = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida.")
    print("Requisitos:")
    print("- Pelo menos 8 caracteres")
    print("- Pelo menos um número")