# Utilizada também para estudar Git.

# Faça um programa, utilizando while, que permita o usuário fazer
# contas de adição enquanto quiser.
# Exercício de revisão

# soma = 0

# num = float(input("Digite um número: "))
# escolha = ''
# while escolha != 'N':
#     soma+= num
#     escolha = input("Deseja adicionar outro número? 'S' para Sim e 'N' para Não: ").upper()
#     match(escolha):
#         case 'N':
#             break
#         case 'S':
#             num = float(input("Digite outro número: "))
# print(f"A soma de todos os números é igual a {soma}.")


# for letra in "Adan Melo Scofield da Silva ":
#     if letra in 'aeiou' or letra in 'AEIOU':
#         print(letra)

# soma = 0 

# for i in range(5):
#     num = float(input("Digite um número: "))
#     soma += num

# print(soma)

# 1. Crie um programa que imprima os números pares de 2 a 10.

# for i in range (0,11,2):
#     print(i)


# Utilize um loop for para calcular o produto dos números de 1
# a 5.

# produto = 1

# for i in range(1,6):
#     produto *= i
# print(produto)

# Crie uma programa que solicite 10 números para o usuário.
# O programa deve somar todos os números múltiplos de 6
# digitados. Se a soma for igual ou maior que 30, o programa
# dever parar e mostrar o resultado da soma.

# soma = 0

# for vezes in range (10):
#     num = int(input("Digite um número: "))
#     if num % 6 == 0:
#         soma += num
#     if soma >= 30:
#         break
# print(f"O resultado da soma dos número: {soma}.")

# Utilize um loop for para imprimir os números de 1 a 20,
# pulando os múltiplos de 3.

# for i in range (1,21, 3):
#      print(i)

# Após ligar o celular, é necessário inserir a senha cadastrada.
# São 3 tentativas até o telefone bloquear. Se o usuário acertar a senha, escreva a mensagem: “bem vindo.”
# Se o usuário errar a senha, escreva a mensagem: “Senha incorretar. Você tem x tentativas até o bloqueio.

senhaCadastrada = input("Cadastre uma senha: ")
senhaEntrada = input("Confirme sua senha: ")
tentativas = 3

while senhaEntrada != senhaCadastrada:
    if tentativas == 0:
        print("Telefone bloqueado!")
        break   
    print(f"Senha incorreta. Você {tentativas} tentativas até o bloqueio.")
    senhaEntrada = input("Digite novamente: ") 
    tentativas -=1

else: 
    print("Bem vindo!")
