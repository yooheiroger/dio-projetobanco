nome = "yoohei"
idade= 30
profissao = "programador"
linguagem = "python"
saldo = 435.3610
dados = {"nome": "yoohei", "idade": 30}

print ("nome: %s idade: %d" % (nome, idade))
print ("nome: {} idade: {}".format(nome, idade))
print ("nome: {1} idade: {0}".format(idade, nome))
print ("nome: {1} idade: {0} nome: {0} {0}".format(idade, nome))
print ("nome: {nome} idade: {idade} nome: {nome} {nome}".format(idade=idade, nome=nome + "\n"))

print ("nome: {nome} idade: {idade}".format(**dados))

print (f"nome: {nome} idade: {idade}" )# o f serve para indicar que essa string tem suas variaveis ja definidas la no comeco e voce pode colocar so as variaveis
print (f"nome: {nome} idade: {idade} saldo: {saldo:.2f}")
