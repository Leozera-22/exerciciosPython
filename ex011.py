print('Calcular quantos litros de tinta preciso')
lar = float(input("Largura da parede(m): "))
alt = float(input("Altura da parede(m): "))
area = lar * alt
tin = area / 2
print("Sua parede tem uma área de {:.3f} m²".format(area))
print("Para pintar essa parede. voce precisa de {:.2f} litros de tinta".format(tin))