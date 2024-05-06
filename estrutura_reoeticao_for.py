# texto = input("infome uma palavra: ")
# VOGAIS = "AEIOU"
# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print (letra, end="")

print ()    # quebra linha  

# RANGE serve para atribur parametros de onde começa ate onde termina e de quanto em quanto vai INICIO 0 ATE 50 e De 5 em 5
for numero in range (0, 51, 5):
    print (numero, end=" " "\n") # end serve para forçar os caracteres aparecerem na mesma linha em sequencia caso contrario fica em colunas sem o end

opcao = -1

while opcao != 0:
    opcao  = int(input("[1] Sacar \n [2] Extrato \n [0] Sair\n"))

    if opcao == 1: 
        print ("Sacando")
    elif opcao == 2:
        print ("Extrato é: ")
else:
    print ("Saindo do programa")    

