#Peça para que o ChatGPT gere para você 5 exercícios de condicionais: 


#1 - Escreva um programa que peça ao usuário para digitar sua idade e determine se ele é elegível para votar ou não (considerando a idade mínima de 18 anos).

# idade = int(input("Digite a sua idade: "))

# if idade >= 18:
#     print("Você pode votar!")
# else: 
#     print("Você ainda não pode votar.")

# 2- Crie um programa que solicite ao usuário que insira um número e determine se é positivo, negativo ou zero.

# num = int(input("Digite um número: "))

# if num > 0:
#     print(f"O número {num} é positivo!")
# elif num < 0:
#     print(f"O número {num} é negativo!")
# else:
#     print("Este número é 0.")

#3- Desenvolva um programa que peça ao usuário para inserir as medidas dos três lados de um triângulo e determine se é um triângulo equilátero, isósceles ou escaleno.

# lados = []

# for iCont in range(0,3):
#      lados.append(int(input(f"Digite o lado {iCont+1} do triângulo: ")))

# if lados[0] == lados[1] and lados[1] == lados[2]:
#     print("Este triângulo é equilátero")
# elif (lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]) and (lados[0] != lados[2] or lados[1] != lados[2] or lados[0] != lados[1]):
#     print("Este triângulo é escaleno.")
# else:
#     print("Este triângulo é isóceles.")

