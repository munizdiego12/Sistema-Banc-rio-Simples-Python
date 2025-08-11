# SISTEMA BANCÁRIO SIMPLES (Diego Muniz)

menu = """
Bem vindo ao Banco, Selecione uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
Digite a opção desejada: 
"""

saldo = 0
saque_maximo = 500
numero_saques = 0
limite_saque = 3
extrato = ""

while True:

    opcao = input(menu)

    if opcao == '1':

        valor = float(input("Opção selecionada: Depósito\nDigite o valor a ser depositado: "))

        if valor < 100:
            print("\nValor mínimo para depósito é R$ 100,00.\nRetomando ao menu principal.")

        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}\nRetomando ao menu principal.")

    elif opcao == '2':

        if numero_saques >= limite_saque:
            print(f"\nNúmero máximo de saques diários atingido.\nRetomando ao menu principal.""")
            continue

        valor = float(input("\nOpção selecionada: Saque\nDigite o valor a ser sacado: "))

        if valor > saque_maximo:
            print(f"\nValor máximo para saque é R$ {saque_maximo:.2f}")

        elif valor > saldo:
            print("\nSaldo insuficiente para saque.\nRetomando ao menu principal.")
            
        else:
            numero_saques += 1
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            print(f"\nSaque realizado com sucesso! Saldo atual: R$ {saldo:.2f}, Saques restantes hoje: {limite_saque - numero_saques}\nRetomando ao menu principal.")

    elif opcao == '3':

        if extrato:
            print("\nExtrato:\n")
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
            
        else:
            print("Nenhuma transação realizada.\nRetomando ao menu principal.")

    elif opcao == '4':
        print("\nSaindo do sistema. Obrigado por usar nossos serviços!")
        break

    else:
        print("\nOpção inválida. Por favor, selecione uma opção válida do menu.")
