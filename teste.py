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

valorHora = int(input("Informe o quanto você ganha por hora: "))
horasTrabalhadas = int(input("informe quantas horas você trabalha por mês: "))
Salario = valorHora * horasTrabalhadas
print(f"Seu salário é {Salario},00 Reais")

#14. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("informe a temperatura em graus fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"A temperatura {fahrenheit}°F quando convertida para graus celsius é de {celsius:.2f}°C")
