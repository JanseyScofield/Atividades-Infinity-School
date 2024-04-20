#Faça um programa que receba 3 números e, ao final,mostre a soma deles (utilizando o WHILE).

iCont = 1;
soma = 0
while iCont <= 3:
    valor = (float(input("Digite um número: ")))
    soma += valor
    iCont += 1

print(f"A soma dos números é: {soma}")
