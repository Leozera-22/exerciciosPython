from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Qual ano você nasceu? "))
idade = ano_atual - ano_nascimento


if idade < 18:
    print("VOCE AINDA NÃO PRECIA SE ALISTAR")
    print("VOCE TEM {}".format(idade))
elif idade == 18:
    print("VA SE ALISTAR URGENTEMENTE!!!!")
    print("VOCE TEM {}".format(idade))
elif idade > 18:
    print("VOCE JA OU DEVERIA TER SE ALISTADO")
    print("VOCE TEM {}".format(idade))

