spuoli = input("Oletko mies vai nainen? ")
hglob = int(input("Mikä on hemoglobiiniarvosi? "))
if spuoli == "mies":
    if hglob < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hglob > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif spuoli == "nainen":
    if hglob < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hglob > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")