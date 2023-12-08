dia = int(input("Quantos dias você usou o carro? "))
km_rodado = float(input("Quantos Km você rodou? "))
preço_dia = dia * 60
preço_km = km_rodado * 0.15
preço_final = preço_dia + preço_km
print("Você precisa pagar R${:.2f} pelo tempo e km rodados com o carro".format(preço_final))
