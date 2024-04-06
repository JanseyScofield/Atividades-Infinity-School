# Implemente um jogo em que o usuário tenta adivinhar um
# número aleatório entre 1 e 20, dando dicas se a tentativa é
# muito alta ou muito baixa.
import random
num = random.randint(1,20)

tentativa = int(input("Digite um número de 1 a 20 para acertar o número secreto: "))
while tentativa != num:
    if num > tentativa:
        tentativa = int(input("O número que você chutou está menor que o secreto. Tente de novo: "))
    elif num < tentativa:
        tentativa = int(input("O número que você chutou está maior que o secreto. Tente de novo: "))
print("Parabéns! Você acertou!")
