def laske_summa(luvut):
    summa = 0

    for luku in luvut:
        summa = summa + luku

    return summa


numerot = [431, 299, 61, 15, 49]

tulos = laske_summa(numerot)

print("Listan lukujen summa on", tulos)
