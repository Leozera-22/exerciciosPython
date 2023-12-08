
num1 = int(input("DIGITE O PRIMEIRO TERMO: "))
razao = int(input("QUAL A RAZAO? "))
decimo = num1 + (10 -1) * razao

for c in range(num1, decimo + razao, razao):
    print("{}".format(c), end= " -> ")
print("ACABOU")
