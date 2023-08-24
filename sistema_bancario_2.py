menu = """
### MENU ###

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = f"""
### EXTRATO ###

"""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Qual valor deseja depositar? "))
        while valor_deposito <= 0:
            valor_deposito = float(input("Por favor, digite um valor positivo. Qual valor deseja depositar? "))
        saldo += valor_deposito
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print(f"O valor de: R${valor_deposito:.2f} foi depositado com sucesso.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Qual valor deseja sacar? "))
            while valor_saque <= 0 or valor_saque > limite or valor_saque > saldo:
                valor_saque = float(input("Valor indisponível. Qual valor deseja sacar? "))
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
        else: 
            print("Limite de saques diários excedido!")

    elif opcao == "e":
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")