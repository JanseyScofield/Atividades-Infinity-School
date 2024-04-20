# Faça um programa que receba uma palavra e mostre
# somente as vogais.

palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
vogaisPalavra = ""
for letra in palavra:
    if letra in vogais:
        vogaisPalavra += letra
        
print(vogaisPalavra)