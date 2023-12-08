salario = float(input("Qual salário do funcionário? R$"))
aumento1 = 0
aumento2 = 0
if salario <= 1250:
    aumento1 = salario * 1.15
    print("O salario que era R${} agora teve um aumento de (15%) e ficou R${}".format(salario, aumento1))
else:
    aumento2 = salario * 1.10
    print("O salario que era R${} agora teve um aumento de (10%) e ficou R${}".format(salario, aumento2))

'''=============<={=P=A=D=R=Ã=O===D=E===C=O=R=E=S===A=N=S=I=}=>==============

->Comando Geral: Dentro de uma str, \033[style;text;backm

        STYLES                     TEXTS                         BACKS
                                                    
0 => none                       30 => preto                     40 => as mesmas cores
1 => negrito                    31 => vermelho                  41 ...
4 => sublinhado                 32 => verde                     42
7 => negativo                   33 => amarelo                   43
                                34 => azul                      44
                                35 => roxo                      45
                                36 => ciano                     46
                                37 => cinza claro               47
                                90 => cinza escuro              100
                                91 => vermelho claro            101
                                92 => verde claro               102
                                93 => amarelo claro             103
                                94 => azul claro                104
                                95 => magenta claro             105
                                96 => ciano claro               106
                                97 => branco                    107
'''