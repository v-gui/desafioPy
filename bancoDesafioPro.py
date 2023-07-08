def menu():

    menu = """
        ================ MENU ================
        [1]\tDepositar
        [2]\tSacar
        [3]\tExtrato    
        [4]\tNovo Usuário
        [5]\tNova Conta
        [6]\tListar Contas
        [7]\tSair

        """
    return input(menu)

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo+=valor
        extrato+= f"Depósito de: R${valor:.2f}\n"    
        print("Depósito realizado!")    
    else:
        print("Ocorreu um erro, certifique-se que o número digitado está correto! ")
    return saldo, extrato

def saque(*,valor,saldo,extrato,limite,numero_saque,limite_saque):
    excedeu_saldo =  valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque

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

    return saldo, extrato, numero_saque

def exibir_extrato(saldo,/,*,extrato):
    print("\nSeu Extrato:")
    print("Não foram realizadas movimentações:" if not extrato else extrato)
    print(f"\nSeu Saldo é:{saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF, apenas números. ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Esse CPF já está cadastrado! ")
        return
    nome = input("Digite Seu nome completo: ")
    dt_nascimento = input("Informe a data do seu nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o seu endereço: (logradouro - num - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "dt_nascimento": dt_nascimento,"cpf": cpf, "endereco":endereco})

    print("Usuário cadastrado! ")

def filtrar_usuario(cpf,usuarios):    
    usuarios_filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtro[0] if usuarios_filtro else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso! ")
        return{"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    else:
        print("Usuário não encontrado! ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
            """
        
        print(linha)

def main():
    LIMITE_SAQUE_DIARIO = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0 
    usuarios = []
    contas = []   

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saque = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUE_DIARIO,                
            )
        
        elif opcao == "3":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)
        
        elif opcao == "5":
            # só funciona porque não possui a opção excluir conta
            numero_conta = len(contas) + 1
            #caso existisse a opção com laço for seria a ideal 
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("\nFinalizando o programa, volte sempre! \n")
            break

        else:
            print("Você digitou uma opção inexistente! ")

main()