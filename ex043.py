print("LOJAS KATIALANDIA") 
valor = float(input("Qual valor da sua compra?"))
print("[1] para pagamento em dinheiro")
print("[2] para pagamento a vista (débito e crédito)")
print("[3] para pagamento no cartão em 2x")
print("[4] para pagamento no cartão em 3x ou mais")

pagamento = int(input("Escolha uma forma de pagamento: "))

if pagamento == 1:
    valor = valor * 0.9
    print("VOCE TEVE UM DESCONTO DE 10%, O VALOR DE SUA COMPRA FICOU R${:.2f}".format(valor))
elif pagamento == 2:
    valor = valor * 0.95
    print("VOCE TEVE UM DESCONTO DE 5%, O VALOR DE SUA COMPRA FICOU R${:.2f}".format(valor))
elif pagamento == 3:
    parcela = valor / 2
    print("SUA COMPRA FICOU COM O VALOR FINAL DE R${:.2f} pago em 2 vezes de".format(valor))
elif pagamento == 4:
    vezes = int(input("EM QUANTAS VEZES? "))
    valor = valor * 1.20
    parcela = valor / vezes
    print("SUA COMPRA TEVE UM ACRESCIMO DE 20% DE JUROS E FICOU COM O VALOR DE {:.2f}".format(valor))
    print("DIVIDIDO EM {} vezes de R${:.2f}".format(vezes, parcela))
