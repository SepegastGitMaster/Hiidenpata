print("Syötä lukuja. Tyhjä kenttä lopettaa operaation.")
luku = input()
if luku != "":
    min = luku
    max = luku
    while luku != "":
        if luku < min:
            min = luku
        if luku > max:
            max = luku
        luku = input()
    print("Pienin luku: ",min)
    print("Suurin luku: ",max)
else:
    print("Et antanut lukuja.")



