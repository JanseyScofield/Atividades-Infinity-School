# Faça um programa que receba vários números e,quando for digitado um valor negativo, mostre a média dos números digitados (não considere o negativo) .

soma = 0;
qtd = 0;
while True:
    n = float(input("Digite um número (digite um número negativo para parar): "))
    if n < 0:
        break
    soma += n
    qtd += 1

media = soma/qtd
print(f"A média foi: {media}")
