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
'''
while True: 
    usuario = input("Digite o nome do úsuario: ")
    senha = input("Digite sua senha: ")
    if usuario == senha:
        print("O usuário e a senha não podem ser idênticos!")
    else:
        print(f"Bem vindo de volta {usuario}!")
        break
'''
#3 Faça um programa que leia e valide as seguintes informações:  
#a) Nome: maior que 3 caracteres;  
#b) Idade: entre 0 e 150;  
#c) Salário: maior que zero;  
#d) Sexo: 'f' ou 'm';  
#e) Estado Civil: 's', 'c', 'v', 'd'
'''
while True:
    nome = input("Digite seu nome: ").strip()
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais de 3 caracteres, tente novamente!")
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade deve estar entre 0 e 150 anos, tente novamente")
    except ValueError:
        print("Digite um número válido para a idade")
while True: 
    try:
        salario = float(input("Digite seu salário: R$"))
        if salario > 0:
            break
        else:
           print("Salário deve ser maior que zero, tente novamente!")
    except ValueError:
            print("Digite um valor numérico válido.")
while True:
        sexo = input("Digite seu sexo (f/m): ").strip().lower()
        if sexo in ['f','m']:
            break
        else:
            print("Sexo deve ser 'f' para feminino e 'm' para masculino.")
while True:
    estado_civil = input("Digite seu estado civil (s-Solteiro, c-Casado, v-Viuvo, d-Divorciado): ").strip().lower()
    if estado_civil in ['s','c','v','d']:
        break
    else:
        print("Estado civil deve ser: s, c, v ou d.")
                
print("Parabéns por completar seu registro!")
'''
            