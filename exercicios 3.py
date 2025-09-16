#1 Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))

        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Valor inválido! A nota deve estar entre 0 e 10.")

    except ValueError:
        print("Valor inválido! Digite apenas números.") 
'''
#2 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True: 
    usuario = input("Digite o nome do úsuario: ")
    senha = input("Digite sua senha: ")
    if usuario == senha:
        print("O usuário e a senha não podem ser idênticos!")
    else:
        print(f"Bem vindo de volta {usuario}!")
        break

#3 Faça um programa que leia e valide as seguintes informações:  
#a) Nome: maior que 3 caracteres;  
#b) Idade: entre 0 e 150;  
#c) Salário: maior que zero;  
#d) Sexo: 'f' ou 'm';  
#e) Estado Civil: 's', 'c', 'v', 'd'