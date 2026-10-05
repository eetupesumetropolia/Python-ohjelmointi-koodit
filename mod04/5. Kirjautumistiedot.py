oikea_tunnus = "testi"
oikea_salasana = "salasana123"

yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yritykset = yritykset + 1

        if yritykset < 5:
            print("Väärä käyttäjätunnus tai salasana")
        else:
            print("Pääsy evätty")
