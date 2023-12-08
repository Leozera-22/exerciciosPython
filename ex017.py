from math import hypot
cat1 = float(input("Digite o valor do primeiro cateto: "))
cat2 = float(input("Digite o valor do segundo cateto: "))
hipo = hypot(cat1, cat2)
print ("A hipotenusa dos catetos {} e {} é {}".format(cat1, cat2, hipo))
