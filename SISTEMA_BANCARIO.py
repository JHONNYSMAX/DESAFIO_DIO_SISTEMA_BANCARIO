menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, informe um valor numérico.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, informe um valor numérico.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "t":
        try:
            valor = float(input("Informe o valor da transferência: "))
            conta_destino = input("Informe a conta de destino: ")

            if valor > 0:
                if valor > saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                else:
                    saldo -= valor
                    extrato += f"Transferência para {conta_destino}: R$ {valor:.2f}\n"
                    print(f"Transferência de R$ {valor:.2f} para a conta {conta_destino} realizada com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, informe um valor numérico.")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")