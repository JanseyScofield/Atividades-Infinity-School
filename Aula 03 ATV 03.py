# Crie um programa que solicite ao usuário adivinhar um
# número entre 1 e 100, dando dicas se a tentativa é muito alta,
# muito baixa ou correta. Adicione um limite de tentativas.

import random
limite = 10
num = random.randint(1,20)
qtdTentativas = 1
tentativa = int(input("Digite um número de 1 a 20 para acertar o número secreto: "))
while tentativa != num:
    if num > tentativa:
        tentativa = int(input("O número que você chutou está menor que o secreto. Tente de novo: "))
    elif num < tentativa:
        tentativa = int(input("O número que você chutou está maior que o secreto. Tente de novo: "))
    qtdTentativas += 1
    if qtdTentativas > limite:
        break
if qtdTentativas > limite:
    print("Você passou do limite de tentativas!")
else:
    print("Parabéns! Você acertou!")
    print(f"Você teve {qtdTentativas} tentativas.")
