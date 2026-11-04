import math


def yksikkohinta(halkaisija, hinta):
    sade_metreina = halkaisija / 2 / 100
    pinta_ala = math.pi * sade_metreina ** 2
    return hinta / pinta_ala


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

print("Ensimmäisen pizzan yksikköhinta on", yksikkohinta1, "euroa/m².")
print("Toisen pizzan yksikköhinta on", yksikkohinta2, "euroa/m².")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzoilla on sama yksikköhinta.")
