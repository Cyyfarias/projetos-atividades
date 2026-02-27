import string

def eh_palindromo(texto):
    texto = texto.lower()
    
    # Remove espaços e pontuação
    texto_limpo = ""
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere
    
    return texto_limpo == texto_limpo[::-1]


# Testando
frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")