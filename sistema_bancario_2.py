import re

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado. Não é possível criar o usuário.")
            return

    cpf_numeros = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos do CPF
    usuario = {'nome': nome, 'cpf': cpf_numeros}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def criar_conta(contas, usuarios):
    cpf_usuario = input("Digite o CPF do usuário para vincular à conta: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return

    numero_conta = len(contas) + 1
    agencia = "0001"
    conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario_encontrado}
    contas.append(conta)
    print("Conta criada com sucesso.")

def listar_contas(contas):
    print("### Lista de Contas ###")
    for conta in contas:
        print(f"Conta: {conta['numero_conta']} - Agência: {conta['agencia']} - Titular: {conta['usuario']['nome']}")

def saque(*, saldo, valor, historico, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > 0 and valor <= limite and valor <= saldo:
            saldo -= valor
            historico += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido.")
    else:
        print("Limite de saques diários excedido!")

    return saldo, historico

def deposito(saldo, valor, historico):
    if valor > 0:
        saldo += valor
        historico += f"Depósito: R${valor:.2f}\n"
        print(f"O valor de: R${valor:.2f} foi depositado com sucesso.")
    else:
        print("Valor de depósito inválido.")

    return saldo, historico

def extrato(saldo, historico):
    print("### Extrato ###")
    print(historico)
    print(f"Saldo atual: R${saldo:.2f}")

def menu():
    usuarios = []
    contas = []
    saldo = 0
    historico = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    limite = 500

    while True:
        opcao = input("""
        ### MENU ###

        [1] Criar Usuário
        [2] Criar Conta Corrente
        [3] Sacar
        [4] Depositar
        [5] Extrato
        [6] Listar Contas
        [q] Sair

        => """)

        if opcao == "1":
            criar_usuario(usuarios)
        elif opcao == "2":
            criar_conta(contas, usuarios)
        elif opcao == "3":
            valor = float(input("Qual valor deseja sacar? "))
            saldo, historico = saque(saldo=saldo, valor=valor, historico=historico, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == "4":
            valor = float(input("Qual valor deseja depositar? "))
            saldo, historico = deposito(saldo=saldo, valor=valor, historico=historico)
        elif opcao == "5":
            extrato(saldo=saldo, historico=historico)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

menu()
