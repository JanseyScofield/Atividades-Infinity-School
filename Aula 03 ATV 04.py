# Crie um programa que solicite ao usuário que digite números inteiros. O programa deve continuar solicitando números até que a soma dos números pares digitados seja maior que 50.Ao atingir ou ultrapassar esse limite, o programa deve exibir a
# soma total e encerrar.Dica: Use um loop while para continuar solicitando números até que a condição seja atendida. Mantenha uma variável para rastrear a soma dos números pares. Utilize a instrução break para sair do loop quando a condição for atendida.
# Exiba a soma total ao final.

somaPar = 0
while somaPar <=50:
    num = int(input("Digite um número: "))
    if num%2 ==0:
        somaPar += num
print(f"O resultado da soma ficou {somaPar}")
