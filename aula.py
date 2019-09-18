idade = int(input("Qual sua idade?"))

if idade >= 21 and idade < 65:
    salario = int(input("Qual seu salário?"))
    emprestimo = int(input("Quanto quer de emprestimo?"))
    print("Idade aceita")
    if emprestimo <= salario*10:
        print("Emprestimo aceito")
    else:
        print("Emprestimo Negado")
else:
    print("Idade recusada")

    # <--- Exemplos Python --->

    cachorros = {"nome": "Tobias", "raça": "pinscher"}

#print(cachorros["nome"], cachorros["raça"])

#print(cachorros.keys())

#print(cachorros.values())

#print(cachorros.items())

#print(cachorros.get("nome"))

#print(cachorros.get("gato", "não existe"))

# <---if/elif/else--->

idade = 19

#if idade > 19:
 #   print("Maior de 18, tome cerveja")
#elif idade == 19:
 #   print("19 anos")
#else:
 #   print("Ainda não, só danoninho")

    # <---function--->


def verrugas(vrs):
    print(vrs + "Verrugas")

#verrugas("strab")

# <---for/in--->

minhalista = ["a", "b", "c", "d"]

#for i in minhalista:
 # print(i)

#for i in range(1,10,2):
 # print(i)

  # <---ordenar(sort)--->

lista1 = [9,4,2,5,8,7]
print(lista1)
lista1.sort()#(reverse.True)
print(lista1)