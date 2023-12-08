from datetime import date
atual = date.today().year
ano = int(input("Qual ano você nasceu?"))
idade = atual - ano

if idade <+ 9:
    print("SUA CATEGORIA É MIRIM, VOCÊ TEM {}".format(idade))
elif idade > 9 and idade <= 14:
    print("SUA CATEGORIA É INFANTIL, VOCÊ TEM {}".format(idade))
elif idade > 14 and idade <= 19:
    print("SUA CATEGORIA É JUNIOR, VOCÊ TEM {}".format(idade))
elif idade > 19 and idade <= 25:
    print("SUA CATEGORIA É SENIOR, VOCÊ TEM {}".format(idade))
else:
    print("SUA CATEGORIA É MASTER, VOCÊ TEM {}".format(idade)) 