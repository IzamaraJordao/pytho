import random
a1 = str (input("Digite o 1º aluno:"))
a2 =  str (input ("Digite o 2º aluno: "))
a3 = str(input("Digite o 3º aluno: "))
a4 = str(input("Digite o 4º aluno: "))
l = [a1, a2, a3, a4]
random.shuffle(l)
print("A ordem de apresentação será:")
print(l)
