saldo = 0
limite = 500
saque = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

print("""
        Bem vindo ao Banco Virtual!

Operações:

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
""")

while True:
    opcao = input("\nEscolha a operação a ser realizada: ").lower()
    if opcao == "d":
        saque = float(input("\nQual o valor do depósito desejado? "))
        if saque > 0:
            saldo += saque
            extrato += f"Valor de depósito: R$ {saque:.2f}\n"
        else:
            print("/nValor de depósito inválido.")

    elif opcao == "s":
        saque = float(input("\nQual o valor do saque desejado? "))
        if numero_saques >= LIMITE_SAQUE:
            print("\nVocê excedeu a quantidade máxima de saques.")
        elif saque > limite:
            print("\nLimite inválido para saque.")
        elif saque > saldo:
            print("\nValor maior que o saldo total.")
        elif saque > 0:
            numero_saques += 1
            saldo -= saque
            extrato += f"O valor do saque realizado: R$ {saque:.2f}\n"

    elif opcao == "e":
        print("\n================ EXTRATO =================")
        print("\nNão foram realizadas operações." if not extrato else extrato)
        print(f"Valor de saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
