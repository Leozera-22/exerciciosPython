viagem = float(input("Qual a distância da viagem?(KM)"))
preço_viagem = 0
if viagem <= 200:
    preço_viagem = viagem * 0.5
    print("Sua viagem vai custar R${:.2f}".format(preço_viagem))
else:
    preço_viagem = viagem * 0.45
    print("Sua viagem vai custar {:.2f}".format(preço_viagem))
