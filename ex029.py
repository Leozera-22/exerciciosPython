velo = float(input('Qual velocidade do carro?'))
multa = (velo - 80) * 7 
if velo <= 80:
    print("Parabens! Diriga com cuidado!") 
else:
    print("Você excedeu o limite da via")
    print("Sua multa é de R${:.2f} ".format(multa))