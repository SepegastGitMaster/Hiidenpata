numero = int(input("Anna kokonaisluku: "))

if numero % 15 == 0:
    print("BoomBuzz")
elif numero % 3 == 0:
    print("Boom")
elif numero % 5 == 0:
    print("Buzz")
else:
    print("Better luck next time!")