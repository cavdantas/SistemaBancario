titulo = "Menu"
titulo_extrato = "Extrato"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
lista_depositos = []
lista_saques = []

def menu():
    print(f"""
        {titulo.center(18)}
        [1] Deposito
        [2] Saque
        [3] Extrato
        [0] Sair
          """)
    
def sacar():
    global saldo, numero_saques, limite, LIMITE_SAQUES, lista_saques
    saque = float(input("Digite o valor que deseja sacar: "))
    if saque <= saldo and saldo > 0 and LIMITE_SAQUES > 0:
        numero_saques += 1
        LIMITE_SAQUES -= 1
        saldo -= saque
        print(f"Operação realizada com sucesso \n Saldo atual: R${saldo:,.2f}")
        lista_saques += [saque]
    else:
        print("Saldo Insuficiente!")

def depositar():
    global saldo, deposito, lista_depositos
    deposito = float(input("Digite o valor que deseja depositar: "))
    if deposito > 0:
        saldo += deposito
        print("Deposito realizado com sucesso!")
        lista_depositos += [deposito]

def funcao_extrato():
    global saldo, limite, numero_saques, LIMITE_SAQUES
    print(titulo_extrato.center(18))
    print(f"Saldo: R${saldo:,.2f} \nNumero de Saques: {numero_saques} \nLimites diario de saques restantes: {LIMITE_SAQUES} \nDepositos: {lista_depositos} \nSaques: {lista_saques}")

menu()
option = int(input("Digite sua opcao: "))

while option != 0:
    if option == 1:
        depositar()
    elif option == 2:
        sacar()
    elif option == 3:
        funcao_extrato()
    else:
        print("Opção Invalida!")
    menu()
    option = int(input("Digite sua opcao: "))

if option == 0:
    print("Operação Finalizada!")