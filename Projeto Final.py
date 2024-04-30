# SIMULADOR DE CADASTRO DE SENHA E INICIALIZAÇÃO DE CELULAR

# Utilizando o aprendizado desta aula, implementaremos um sistema de cadastro de senha e inicialização do celular utilizando o loop "for".

# Após ligar o celular, o usuário é solicitado a inserir a senha cadastrada.
# São permitidas 3 tentativas até que o telefone seja bloqueado.
# Se o usuário acertar a senha, uma mensagem de boas-vindas é exibida: "Bem-vindo."
# Se o usuário errar a senha, uma mensagem informando o erro é exibida, junto com o número de tentativas restantes até o bloqueio do telefone.
# Pense em todas as possibilidades e faça um sistema completo.

senhaCadastrada = input("Crie uma senha: ")
tentativas = 3

while  tentativas >  0:
    senhaEntrada = input("Digite a senha: ")
    if senhaCadastrada != senhaEntrada and tentativas > 0:
        tentativas  -=  1
        print(f"Senha incorreta! Tente novamente. Lhe resta {tentativas} tentativas.")
    else:
        break

if  tentativas> 0:
    print("Telefone desbloqueado com sucesso!")
else:
    print("Telefone bloquedo!")
