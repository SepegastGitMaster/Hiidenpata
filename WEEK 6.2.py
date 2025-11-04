import random
def heitto(tahkot):
    return random.randint(1, tahkot)
tahkot = int(input("Heitetään noppaa, mutta anna ensin nopan tahkojen määrä!"))
while True:
    tulos = heitto(tahkot)
    print(f"Heitit {tulos}")
    if tulos == tahkot:
        break
