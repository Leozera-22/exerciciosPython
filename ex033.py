num1 = float(input("DIGITE UM VALOR:"))
num2 = float(input("DIGITE UM VALOR:"))
num3 = float(input("DIGITE UM VALOR:"))

menor = num1
maior = num2

if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3

if num1 > num2 and num1 > num3:
    maior = num1
if num3 > num2 and num3 > num1:
    maior = num3

print ("Maior valor {} e menor valor {}".format(maior, menor))