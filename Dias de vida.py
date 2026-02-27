from datetime import date

# Entrada da data de nascimento
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

data_nascimento = date(ano, mes, dia)
data_atual = date.today()

diferenca = data_atual - data_nascimento

print(f"Você está vivo há {diferenca.days} dias.")