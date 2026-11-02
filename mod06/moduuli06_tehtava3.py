def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


gallonat = float(input("Anna bensiinimäärä gallonoina: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print(gallonat, "gallonaa on", litrat, "litraa.")

    gallonat = float(input("Anna bensiinimäärä gallonoina: "))
