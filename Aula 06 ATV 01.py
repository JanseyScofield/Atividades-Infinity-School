# 1. Faça um programa que peça 4 notas de um aluno (utilizando estruturas de repetição) e mostre a média delas.

soma = 0;

for cont in range(1,5):
    n = float(input(f"Digite a nota {cont}: "))
    soma += n;

media = soma/4;

print(f"A sua média foi de: {media}")
