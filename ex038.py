num1 = int(input("DIGA UM NUMERO: "))
num2 = int(input("DIGA OUTRO NUMERO: "))

if num1 > num2:
    print("{} é maior que {}".format(num1, num2))
elif num2 > num1:
    print("{} é maior que {}".format(num2, num1))
else:
    print("OS VALORES SÃO IGUAIS!!!")
