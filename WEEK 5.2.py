print("Syötä vähintään viisi kokonaislukua. Tyhjä kenttä lopettaa operaation.")
annetut_luvut = []
while True:
    x = input()
    if x == "":
        break
    else:
        luku = int(x)
        annetut_luvut.append(luku)
annetut_luvut.sort(reverse=True)
print("Antamistasi luvuista viisi suurinta ovat")
for luku in annetut_luvut[0:5]:
    print(luku)

#Miksei ekaa syötettyä lukua lasketa mukaan?
#ratkesi kun poistin turhan "luku = int(input())" tosta alusta - TSEKKAA ETTEI SILMUKAN ULKOPUOLELLA OO OLENNAISIA JUTTUJA!!!
