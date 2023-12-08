num = int(input("Digite um numero: "))
escolha = int(input("Qual base voce quer tranformar seu numero? Digite (1) para binário, (2) para hexa e (3) para octa: "))

if escolha == 1:
    print(bin(num))
elif escolha == 2:
    print(hex(num))
elif escolha == 3:
    print(oct(num))
else:
    print("VALOR DIGITADO INVALIDO, TENTE OUTRO!!!")


#num = int(input("DIZ AI:"))
#print(bin(num))

