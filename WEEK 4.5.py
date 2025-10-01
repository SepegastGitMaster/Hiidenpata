print("Syötä kirjautumistiedot")
tunnus = "python"
sana = "rules"
yritys = 0
while True:
    if yritys == 5:
        print("\nPääsy evätty.")
        break
    t_arvaus = input("\nKäyttäjätunnus: ")
    s_arvaus = input("Salasana: ")
    if t_arvaus == tunnus and s_arvaus == sana:
        print("\nTervetuloa!")
        break
    yritys = yritys + 1