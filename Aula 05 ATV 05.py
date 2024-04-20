#Faça um programa em que o usuário só possa digitar valores numéricos. Caso ele digite uma letra, mostre uma mensagem de erro e peça novamente um valor.

num = input("Digite um número: ")

while not num.isdigit():
    print("Não é um número!")
    num = input("Digite um número: ")
