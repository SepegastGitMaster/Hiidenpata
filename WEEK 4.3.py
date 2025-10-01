print("Syötä lukuja. Tyhjä kenttä lopettaa operaation.")
luku = int(input())
maxi = luku
mini = luku
while True:
    x = input()
    if x == "":
        break
    else:
        luku = int(x)
    if luku < mini:
        mini = luku
    if luku > maxi:
        maxi = luku
print("Pienin luku: ",mini)
print("Suurin luku: ",maxi)



