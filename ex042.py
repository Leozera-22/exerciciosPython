print("----" * 12)
print('IMC PARA IDOSOS')
print("----" * 12)
peso = float(input("Qual o seu peso? (kg)"))
altura = float(input("Qual a sua altura? (m)"))
print("NÃO ACEITAMOS NÃO BINARIOS OK?")
imc = peso / altura ** 2

if imc <= 22:
    print("BAIXO PESO SENHOR(A), PROCURE UMA NUTRI URGENTE!!!!!")
elif imc > 22 and imc <= 27:
    print("EUTROFIA (NORMAL) TA SUAVE VELHÃO VAI CURTIR OS NETOS")
else:
    print("EXCESSO DE PESO SENHOR(A), POR FAVOR PROCURE UMA SMARTFIT. APENAS R&9,90 O PRIMEIRO MÊS ")    









#peso / altura ao quadrado