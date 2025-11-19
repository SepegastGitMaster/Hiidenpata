nimet = set()
while True:
    nimi = input("Anna nimi (syötä tyhjä kenttä lopettaaksesi): ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi\n")
    else:
        print("Uusi nimi\n")
        nimet.add(nimi)
print(nimet)