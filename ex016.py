preco_casa = float(input("Qual valor da casa?"))
salario = float(input("Qual seu salario?"))
ano = int(input("Em quantos anos deseja pagar?"))
prestacao = preco_casa / (ano * 12)

if prestacao >= (salario * 0.30):
    print("EMPRESTIMO NEGADO SUA PRESTAÇÃO DE {} É MAIOR QUE O MINIMO ACEITO PARA SUA RENDA".format(prestacao))
elif prestacao < (salario * 0.30):
    print ("EMPRESTIMO ACEITOE SUA PRESTAÇÃO SERÁ DE {:2.f}").format(prestacao)