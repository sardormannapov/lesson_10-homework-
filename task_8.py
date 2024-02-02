alph = ["a", "ccc", "dddd", "bb"]
summa = 0
while summa < len(alph):
    summa2 = summa + 1
    while summa2 < len(alph):
        if len(alph[summa]) > len(alph[summa2]):
            alph[summa], alph[summa2] = alph[summa2], alph[summa]
        summa2 += 1
    summa += 1
print(alph)