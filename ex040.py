nota1 = float(input("Qual foi a primeira nota? "))
nota2 = float(input("Qual foi a segunda nota? "))
media = (nota1 + nota2) / 2
if media >= 6:
    print("VOCE FOI APROVADA COM A MEDIA DE {:.2f} PONTOS".format(media))
elif media < 6 and media >= 4:
    print("VOCE ESTA DE RECUPERAÇÃO COM A MEDIA DE {:.2F} PONTOS".format(media))
else:
    print("SE FUDEO, TA REPROVADO!")
