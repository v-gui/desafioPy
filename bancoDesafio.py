# 1° Versão = 3 operações, depósito, saque e extrato
# deposito = 1 usuario.
# saques = 3 saques diarios/R$500,00 limite

menu = """
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato    
    [4]\tSair

    """

saldo = 0
limite_saque = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3



while True:

    opcao =input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo+=valor
            extrato+= f"Depósito de: R${valor:.2f}\n"
        
        else:
            print("Ocorreu um erro, certifique-se que o número digitado está correto! ")
    
    elif opcao == "2":
        valor = float(input("Digite a quantidade que deseja sacar: "))

        excedeu_saldo =  valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não possui saldo suficiente para executar a transação! ")

        elif excedeu_limite:
            print("Certifique-se que a quantidade digitada para saque não ultrapasse R$500,00! ")

        elif excedeu_saques:
            print("Seu plano possui apenas 3 saques diários, tente novamente amanhã! ")

        elif valor >0:
            saldo -= valor
            extrato += f"Saque de: R${valor:.2f}\n"
            print("Saque concluído")
            numero_saque += 1
            
        else:
            print("Operação falhou, valor informado é inválido! ")

    elif opcao == "3":
        print("\nSeu Extrato:")
        print("Não foram realizadas movimentações:" if not extrato else extrato)
        print(f"\nSeu Saldo é:{saldo:.2f}")

    elif opcao == "4":
        break
    
    else:
        print("Operação inválida, por favor selecione o número corretamente! ")