
s = 0

for c in range(3, 501, 3):
    if c % 2 != 0:
        s = s + c

print("A soma dos termos é {}".format(s))