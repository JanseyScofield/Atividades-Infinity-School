# Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.Exercício de revisão

soma = 0

num = float(input("Digite um número: "))
escolha = ''
while escolha != 'N':
    soma+= num
    escolha = input("Deseja adicionar outro número? 'S' para Sim e 'N' para Não: ").upper()
    match(escolha):
        case 'N':
            break
        case 'S':
            num = float(input("Digite outro número: "))
print(f"A soma de todos os números é igual a {soma}.")



