from random import randint
from time import sleep

itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)

print("SUAS OPÇÕES:")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogador = int(input("ESCOLHA SUA OPÇÃO: "))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.5)

print("O computador jogou...{}".format(itens[computador]))
print("O jogador jogou...{}".format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")





