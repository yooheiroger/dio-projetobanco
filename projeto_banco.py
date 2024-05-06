saldo = 0
extrato = 0
numero_saque = 0
limite_saque = 500
LIMETE_SAQUE_CONTA = 3
valor_saque = 0
deposito = 0

menu = """
****Escolha uma opção****

    [a] Sacar
    [b] Depositar
    [c] Extrato
    [d] Sair
*************************
"""

print("Escolha uma opção: ")

while True:
    opcao=input(menu)

    if opcao == "b":
        deposito = float(input("Digite o valor a ser depositado: "))
        
        if deposito > 0:
            extrato = deposito
            saldo = deposito
            print ("Deposito realizado com sucesso")
        
        else: 
            print ("Valor não compativel")

    
    
    elif opcao == "a":
        
        valor_saque = float(input("Digite um valor: ")) 
        if limite_saque < valor_saque:
            print ("Excedeu o valor do saque\n")
        elif saldo < valor_saque:
            print ("Valor indisponivel para saque\n")
        elif numero_saque > 3:
            print ("Excedeu o numero de saques diarios\n")
        elif numero_saque == 3:
            print("Quantidade de saques diarios execida\n")
        else:
            numero_saque += 1
            print ("Seu saque foi de: ", valor_saque, "\n")      
            print(numero_saque)
    elif opcao == "c":
        extrato -=valor_saque
        print("seu extrato bancario\n")
        print("******Extrato******\n")
        print("valor depositado: ", deposito)
        print ("Valor sacado: ", valor_saque)
        print("Valor em conta, R$ ",extrato,"\n")

    elif opcao == "d":
        print ("Finalizando seção, obrigado por utilizar nosso banco")
        break
    else:
        print("Comando invalido tente novamente \n")        
        