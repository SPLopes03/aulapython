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