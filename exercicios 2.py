#01 Crie uma variável chamada "idade" e atribua um valor inteiro a ela. 
#Verifique se a idade é maior ou igual a 18 e imprima "Maior de idade" ou "Menor de idade" de acordo com a condição. 
"""
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
    """
#02 Crie uma variável chamada "número" e atribua um valor inteiro a ela. 
#Verifique se o número é positivo, negativo ou zero e imprima a mensagem correspondente.
"""
numero = 0
if numero > 0:
    print("Número positivo")
elif numero == 0:
    print("Número é zero")
else:
    print("Número Negativo")
"""
#03 Crie duas variáveis, "nota1" e "nota2", e atribua valores numéricos a elas. 
#Verifique se a média das notas é maior ou igual a 7 e imprima "Aprovado" ou "Reprovado" de acordo com a condição. 
"""
nota1 = 7
nota2 = 7
media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Sua média é {media} você esta aprovado!")
else:
    print(f"Sua média é {media} você esta reprovado!")
"""
#04 Crie uma variável chamada "idade" e atribua um valor inteiro a ela. Verifique se a idade está dentro do intervalo
# de 18 a 30 (inclusive) e imprima a mensagem "Idade válida" ou "Idade inválida" de acordo com a condição.
"""
idade = 30
if idade >= 18 and idade <= 30:
    print("Sua idade é valida")
else:
    print("Sua idade não é valida")
"""
#05 Crie uma variável chamada "numero" e atribua um valor inteiro a ela. Verifique se o número é par ou ímpar e imprima a mensagem correspondente.
"""
numero = 10
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")
"""
#06 Crie uma variável chamada "horario" e atribua um valor inteiro representando a hora do dia
#(em formato 24 horas). Verifique se o horário está dentro do período da manhã (das 6h às 12h),
#da tarde (das 12h às 18h) ou da noite (das 18h às 23h) e imprima a mensagem correspondente.
"""
horario = 24
if horario >= 6 and horario <= 12:
    print("Horário da manhã")
elif horario > 12 and horario <= 18:
    print("Horário da tarde")
elif horario > 18 and horario <= 23:
    print("Horário da noite")
else: 
    print("Horário da madrugada")
"""
#07 Crie uma variável chamada "peso" e atribua um valor numérico a ela. Verifique se o peso está dentro do 
#intervalo de 50 a 100 (inclusive) e imprima a mensagem "Peso válido" ou "Peso inválido" de acordo com a condição. 
"""
peso = 101
if peso >= 50 and peso <=100:
    print("Peso valido!")
else:
    print("Peso Inválido!")
"""
#08 Crie uma variável chamada "numero" e atribua um valor inteiro a ela. Verifique se o número é múltiplo de 3 e de 5 ao mesmo tempo e imprima a mensagem correspondente.
numero = 10
if numero % 3 == 0 and numero % 5 == 0:
    print("O numéro é multiplo de 3 e 5")
else:
    print("O numero não é multiplo de 3 e 5")