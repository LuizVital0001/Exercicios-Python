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
"""
numero = 10
if numero % 3 == 0 and numero % 5 == 0:
    print("O numéro é multiplo de 3 e 5")
else:
    print("O numero não é multiplo de 3 e 5")
"""
#09 Crie uma variável chamada "ano" e atribua um valor inteiro representando um ano.
#Verifique se o ano é bissexto (divisível por 4, mas não por 100, exceto se for divisível 
#por 400) e imprima a mensagem correspondente.
"""
ano = 2020
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano Bissexto")
else:
    print("Ano não é bissexto")
"""    
#10 Crie uma variável chamada "salario" e atribua um valor numérico a ela. Verifique se 
#o salário é maior do que 1000 e menor do que 2000 ao mesmo tempo e imprima a mensagem correspondente.
"""
salario = 900
if salario >= 1000 and salario <= 2000:
    print(f"Seu salário é R${salario},00 e esta entre R$1000,00 e R$2000,00")
else:
    print(f"Seu salário é de R${salario},00 e não atende aos requisitos")
"""
#11  Faça um Programa que peça dois números e imprima o maior deles.
"""
num1 = 20
num2 = 20
if num1 > num2:
    print(f"O número {num1} é o maior")
elif num2 > num1:
    print(f"O número {num2} é o maior")
else:
    print("Os números são iguais")
"""
#12 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
"""
numero = -10
if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print("Zero é um valor neutro")
"""
#13Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = input("Digite a letra correspondente ao seu sexo: ").upper()
if sexo == "F":
    print("Sexo Feminino")
elif sexo == "M":
    print("Sexo Masculino")
else:
    (print("Sexo Inválido"))
"""
#14 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite qualquer letra do alfabeto: ").upper()
if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")

#15