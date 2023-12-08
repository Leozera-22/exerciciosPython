from datetime import date

ano = int(input('Digite um ano para analisar se é bissexto! Digite 0 para alisar ano atual'))

if ano == 0:
    ano = date.today().year()

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ("ANO BISSEXTO")
else: 
    print("ANO NÃO BISSEXTO")