# 1.Criando um programa para receber dois valores e em seguida, exibir o valor da soma.
'''
num1 = int(input( "digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))
soma = num1 + num2
print(soma)
'''
#2. Crie um programa para receber dois valores e em seguida, exiba o valor da diferença entre eles. 
""""
num1 = int(input("informe o primeiro valor: "))
num2= int(input("informe o segundo valor: "))
diferenca = num1 - num2
print(diferenca)
"""
#3.Crie um programa para receber dois valores e em seguida, exiba o produto entre eles.
"""
num1 = int(input("informe o primeiro valor: "))
num2 = int(input("informe o segundo valor: "))
produto = num1 * num2
print(produto)
"""
#4.Crie um programa para receber dois valores e em seguida, exiba o quociente entre eles.
"""
num1 = int(input("informe o primeiro valor: "))
num2 = int(input("informe o segundo valor: "))
quociente = num1 / num2
print(quociente)
"""
#5. Crie um programa para receber dois valores e em seguida, exiba o resto da divisão entre eles. 
"""
num1 = float(input("informe o primeiro valor: "))
num2 = float(input("informe o segundo valor: "))
resto = num1 % num2
print(resto)
"""
#6.Crie um programa para receber um número e em seguida, exiba o quadrado dele.
"""
num = float(input("informe o valor: "))
quadrado = num ** 0.5
print(quadrado)
"""
#7.Elabora um programa para calcular a raiz quadrada de um número, utilizando a biblioteca math.
"""
import math 
num = float(input("informe o número: "))
raiz_quadrada = math.sqrt(num)
print(raiz_quadrada)
"""
#8. Crie um programa que seja capaz de calcular o valor absoluto de um número. 
"""
num = -5
absoluto = abs(num)
print (absoluto)
"""
#9. Quais são os tipos das variáveis abaixo?:  
"""
var1 = 347 #int
var2 = 2.71 #float
var3 = "347" #string
var4 = 2+3j #Números Complexos
"""
#10. Faça um Programa que converta metros para centímetros. 
"""
metro = float(input("Informe a quantidade de metros para conversão: "))
centimetro = metro * 100
print(f"{metro} metros é igual a {centimetro} centimetros")
"""
#11.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
raio = float(input("informe o raio do circulo: "))
area = 3.14159 * (raio ** 2)
print(f"A aréa do círculo com raio {raio} é: {area:2f}")
"""
#12. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
lado = 10
area = lado ** 2
resultado = area + area
print((f"O dobro da area do quadrado é {resultado}"))
"""
#13.  Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês. 
"""
valorHora = int(input("Informe o quanto você ganha por hora: "))
horasTrabalhadas = int(input("informe quantas horas você trabalha por mês: "))
Salario = valorHora * horasTrabalhadas
print(f"Seu salário é {Salario},00 Reais")
"""
#14. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
"""
fahrenheit = float(input("informe a temperatura em graus fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"A temperatura {fahrenheit}°F quando convertida para graus celsius é de {celsius:.2f}°C")
"""
#15. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre a temperatura em graus Fahrenheit.
"""
celsius = float(input("informe a temperatura em graus celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura {celsius}°C quando convertida para graus Fahrenheit é de {fahrenheit:.2f}°F")
"""
#16 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
#a) o produto do dobro do primeiro com metade do segundo. 
#b) a soma do triplo do primeiro com o terceiro. 
#c) o terceiro elevado ao cubo.
"""
n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))
n3 = float(input("Informe o número real: "))

result1 = (n1 * 2) * (n2 / 2)
result2 = (n1 * 3) + n3
result3 = (n3 ** 3)

print(f"O primeiro resultado é {result1}")
print(f"O segundo resultado é {result2}")
print(f"O terceiro resultado é {result3}")
"""
#17 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso
# de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.
"""
peso = float(input("Informe a quantidade de peixes em kilos: "))
excesso = max(0, peso - 50)
multa = excesso * 4.00

print("-Resumo-")
print(f"Peso: {peso} kg")
print(f"Excesso: {excesso:.2f} kg")
print(f"Multa: R$ {multa:.2f}")
"""
#18 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto.  
#b) quanto pagou ao INSS.  
#c) quanto pagou ao sindicato.  
#d) o salário líquido.  
#e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valorHora = int(input("Informe o quanto você ganha por hora: "))
horasTrabalhadas = int(input("informe quantas horas você trabalha por mês: "))
salario = valorHora * horasTrabalhadas
print(f"+ Salário Bruto: R${salario}")

ir = salario * 11 / 100
inss = salario * 8 / 100
sindicato = salario * 5 / 100
salario_liquido = salario - ir - inss - sindicato

print(f"- IR (11%): R${ir}")
print(f"- INSS (11%): R${inss}")
print(f"- Sindicato (11%): R${sindicato}")
print(f"= Salário Liquido: R${salario_liquido}")

