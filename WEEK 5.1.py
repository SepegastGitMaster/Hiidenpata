import random
monta_noppaa = int(input("Kuinka montaa noppaa heitetään? "))
summa = 0
for i in range(monta_noppaa):
    heitto = random.randint(1, 6)
    print("Heitit", heitto)
    summa = summa + heitto
print("Heitettyjen lukujen summa on", summa)