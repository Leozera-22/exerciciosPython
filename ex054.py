from datetime import date
atual = date.today().year

maior = 0
menor = 0

for c in range (1, 8):
    ano = int(input("EM QUE ANO A {}° PESSOA NASCEU? ". format(c)))
    idade = atual - ano 
    if idade >= 18:
       maior += 1
    else:
       menor += 1
print("TEM {} MAIORES DE IDADE".format(maior))
print("TEM {} MENORES DE IDADE".format(menor))


