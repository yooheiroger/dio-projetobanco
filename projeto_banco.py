saldo = 0
extrato = 0
numero_saque = 0
limite_saque = 500
LIMETE_SAQUE = 3

menu = """

    [1] Sacar
    [2] Depositar
    [3] Extrato
    [0] Sair

"""

print("Escolha uma opção: ", menu)

while True:
    opcao=input(menu)

    if opcao == 2:
        deposito = float(input("Digite o valor a ser depositado: "))
        
        if deposito > 0:
            extrato = deposito
            print ("Deposito realizado com sucesso")
        
        else: 
            print ("Valor não compativel")

    
    
    elif opcao == 1:
        
        valor_saque = float(input("Digite um valor: ")) 
        if valor_saque > limite_saque:
            print ("Excedeu o valor do saque")
        elif saldo < valor_saque:
            print ("Valor indisponivel para saque")
        elif numero_saque > 3:
            print ("Excedeu o numero de saques diarios")
        elif valor_saque > LIMETE_SAQUE:
            print("Excedeu o valor de saque")
        else:
            numero_saque += 1
            print ("Seu saque foi de: ", valor_saque)      
    
    elif opcao == 3:
        print("seu extrato bancario")
        print("******Extrato******")
        print("valor depositado: ", deposito)
        print ("Valor sacado: ", valor_saque)
        print("R$ ",extrato)

    elif opcao == 0:
        print ("Finalizando seção, obrigado por utilizar nosso banco")
        break
    else:
        print("Comando invalido tente novamente \n")        
        