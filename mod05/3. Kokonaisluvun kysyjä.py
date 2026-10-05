while True:
    syote = input("Anna kokonaisluku: ")

    try:
        luku = int(syote)
        break
    except ValueError:
        print("Virheellinen syöte. Anna kokonaisluku.")

alkuluku = True

if luku < 2:
    alkuluku = False
else:
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            alkuluku = False
            break

if alkuluku:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")
