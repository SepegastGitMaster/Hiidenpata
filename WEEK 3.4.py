print("\nTERVETULOA KARKAUSVUOSITARKASTAJAAN\n")
vuosi = int(input("Syötä vuosi: "))
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print("Antamasi vuosi on karkausvuosi!")
    else:
        print("Antamasi vuosi ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print("Antamasi vuosi on karkausvuosi!")
else:
    print("Antamasi vuosi ei ole karkausvuosi.")