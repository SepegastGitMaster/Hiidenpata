import random
numero = random.randint(1,10)
arvaus = int(input("Arvaa oikea numero 1:n ja 10:n väliltä!"))
while True:
    if arvaus < numero:
        print("Liian pieni arvaus. Uudestaan!")
    if arvaus > numero:
        print("Liian suuri arvaus. Uudestaan!")
    if arvaus == numero:
        print("Oikein!")
        break
    arvaus = int(input())