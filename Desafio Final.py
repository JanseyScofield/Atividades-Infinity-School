# Faça um Programa que registrará as vendas de uma loja. Cada venda conterá:
# Nome do Comprador
# Preço da Compra
# A cada venda o programa deve perguntar: “Deseja registrar mais uma venda?” O usuário deve responder com “S” ou “N” para a pergunta. Essa resposta deve ser tratada, não permitindo números ou palavras com mais uma letra. Além disso, o programa deve aceitar a resposta independentemente dela ser maiúscula ou minúscula. Ao final do programa, ele deve mostrar o faturamento total do dia e qual foi o comprador que gastou mais na loja.

faturamentoTotal = 0 
maiorComprador = ''
maiorCompra = 0

while True:
    nomeComprador = input("Digite o nome do comprador: ")
    valorCompra = float(input("Digite o valor da compra: "))
    faturamentoTotal += valorCompra
    if valorCompra > maiorCompra:
        maiorCompra = valorCompra
        maiorComprador = nomeComprador
    escolha = input("Deseja registrar mais uma venda? S ou N?").upper()
    while escolha != "S" and escolha != "N":
        escolha = input("Valor inválido! Digite novamente S ou N: ").upper()
    if escolha == "S":
        continue
    elif  escolha == "N":
        break

print(f"O faturamento total do dia foi: {faturamentoTotal}")
print(f"O maior comprador foi: {maiorComprador}")