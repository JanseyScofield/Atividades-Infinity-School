#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
#5% para o sindicato, faça um programa que nos dê:
#Salário bruto.
#Quanto pagou ao INSS.
#Quanto pagou ao sindicato.
#O salário líquido.
#Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#Salário Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$
#Salário Liquido : R$

horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valorHora = float(input("Digite o valor por hora trabalhada: "))

salarioBruto = horasTrabalhadas * valorHora
ir = salarioBruto*(11/100)
inss = salarioBruto*(8/100)
sindicato = salarioBruto*(5/100)
salarioLiquido = salarioBruto - ir - inss - sindicato
print(f"Salário bruto: R$ {salarioBruto};\nIR: R$ {ir};\nINSS: R$ {inss};\nSindicato: R$ {sindicato};\nSalário Líquido: R$ {salarioLiquido}.")
