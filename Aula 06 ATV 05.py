# Faça um programa que receba um número “n” e mostre a sequência de Fibonacci até o enésimo elemento.

n = int(input("Digite o enésio termo da sequência de Fibonacci: "))

num = 1
ant = 0
aux = 0
for x in range(n):
    print(num)
    aux = ant
    ant = num
    num = ant + aux
