frase = str(input("DIGITE UMA FRASE: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print("PALINDROMO")
else:
    print("NÃO É PALINDROMO")

