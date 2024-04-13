senhaCadastrada = input("Cadastre uma senha: ")
senhaEntrada = input("Confirme sua senha: ")
tentativas = 3

while senhaEntrada != senhaCadastrada:
    if tentativas == 0:
        print("Telefone bloqueado!")
        break   
    print(f"Senha incorreta. Você {tentativas} tentativas até o bloqueio.")
    senhaEntrada = input("Digite novamente: ") 
    tentativas -=1

else: 
    print("Bem vindo!")
