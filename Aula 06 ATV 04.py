# Faça um programa que receba um número e diga se esse número é primo ou não.
n = int(input("Digite um número: "))
div = 0

for iCont in range (1, n + 1):
    if n % iCont == 0:
        div += 1
    
if div == 2:
    print(f"{n} é primo!")
else:
    print(f"{n} não é primo!")
