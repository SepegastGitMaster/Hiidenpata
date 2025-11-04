def muunnos(gal):
    litr = gal * 3.785
    return litr
while True:
    gallonat = float(input("Anna bensiinin määrä gallonissa: "))
    if gallonat < 0:
        print("Syötit negatiivisen arvon - Aloita ohjelma alusta.")
        break
    litrat = muunnos(gallonat)
    print(gallonat," gallonaa on ", litrat, "litraa.\n")