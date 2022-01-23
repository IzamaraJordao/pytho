import random
a1 = input("digite o nome do 1º aluno: ")
a2 =input("Digite o nome do 2º aluno: ")
a3 = input("Digite o nome do 3º aluno: ")
a4 = input("digite o nome do 4º aluno: ")

lista = [a1,a2,a3,a4]
s = random.choice (lista)
print("O aluno sorteado foi {}".format(s))
