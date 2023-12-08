sal = float(input("Qual seu salário atual? "))
#aumento = sal * 1.15#
aumento = sal * 0.15
novo_sal = sal + aumento
print("Seu salário anterior era R${:.2f}, agora com aumento de 15% será R${:.2f}".format(sal, novo_sal))