lentoasemat = {"EGLL": "London Heathrow Airport",
    "LFPG": "Paris Charles de Gaulle Airport",
    "EHAM": "Amsterdam Schiphol Airport",
    "EDDF": "Frankfurt am Main Airport",
    "LEMD": "Madrid Barajas Airport",
    "LEBL": "Barcelona El Prat Airport",
    "EDDM": "Munich Airport",
    "LIRF": "Rome Fiumicino Airport",
    "EGKK": "London Gatwick Airport",
    "EFHK": "Helsinki-Vantaan Lentoasema"
}
while True:
    valinta = input("\nValitse toiminto:\n [1] Syötä uusi lentoasema\n [2] Hae lentoasemaa\n [3] Lopeta ohjelma\n")
    if valinta == "3":
        print("Ohjelma lopetettu.")
        break
    elif valinta == "1":
        print("Luodaan tietokantaan uusi lentoasema.")
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
        asema = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = asema
    elif valinta == "2":
        print("Lentokenttähaku. ")
        icao = input("Syötä haettavan lentoaseman ICAO-koodi:").upper()
        if icao in lentoasemat:
            asema = lentoasemat[icao]
            print("ICAO-koodia vastaava lentoasema on", asema)
        else:
            print("Lentoasemaa ei löydy tietokannasta.")
    else:
        print("Virheellinen valinta.")

