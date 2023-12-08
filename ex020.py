from random import shuffle
aluno1 = str(input("PRIMEIRO ALUNO: "))
aluno2 = str(input("SEGUNDO ALUNO: "))
aluno3 = str(input("TERCEIRO ALUNO: "))
aluno4 = str(input("QUARTO ALUNO: "))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem de apresentação é: {}".format(lista))