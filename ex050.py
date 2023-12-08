soma = 0

for c in range(1, 7):
    num = int(input("DIGITE UM NUMERO: "))
    if num % 2 == 0:
        soma = soma + num 
print("A SOMA DOS NUMEROS PARES É {}".format(soma))