import random
def heitto():
    return random.randint(1, 6)
print("Heitetään noppaa!")
while True:
    tulos = heitto()
    print(f"Heitit {tulos}")
    if tulos == 6:
        break
