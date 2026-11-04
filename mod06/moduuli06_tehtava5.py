def poista_parittomat(luvut):
    parilliset = []

    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset


alkuperainen_lista = [1965, 462, 3453, 434, 7865345, 34256, 776, 8654]

karsittu_lista = poista_parittomat(alkuperainen_lista)

print("Alkuperäinen lista:", alkuperainen_lista)
print("Karsittu lista:", karsittu_lista)
