num = int(input("DIGITE UM NUMERO PARA SUA TABUADA: "))
result = 0
for cont in range(0, 11):
    result = cont * num
    print ("{} X {} = {}".format(num, cont, result))
print("ESSA É A TABUADA DO {} ATÉ 10".format(num))