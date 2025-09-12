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

var1 = 347 #int
var2 = 2.71 #float
var3 = "347" #string
var4 = 2+3j #Números Complexos

#10. Faça um Programa que converta metros para centímetros. 
metro = float(input("Informe a quantidade de metros para conversão: "))
centimetro = metro * 100
print(f"{metro} metros é igual a {centimetro} centimetros")