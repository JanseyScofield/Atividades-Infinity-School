# Faça um programa que peça 5 números e mostre o maior entre eles.

numMaior = float()
for i in range(0,5):
    valor = (float(input("Digite um número: ")))
    if valor >= numMaior:
        numMaior = valor
print(f"O maior número é: {numMaior}")
    
