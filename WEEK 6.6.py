import math
def pizzan_arvo(halkaisija,hinta):
    pinta_ala = ((halkaisija / 2) / 100) ** 2 * math.pi
    return hinta / pinta_ala

halkaisija1 = float(input("Mikä on ensimmäisen pizzan halkaisija? "))
hinta1 = float(input("entä hinta? "))
halkaisija2 = float(input("Mikä on toisen pizzan halkaisija? "))
hinta2 = float(input("entä hinta? "))

ekan_pizzan_neliohinta = pizzan_arvo(halkaisija1,hinta1)
tokan_pizzan_neliohinta = pizzan_arvo(halkaisija2,hinta2)

if ekan_pizzan_neliohinta < tokan_pizzan_neliohinta:
    print("Osta ensimmäinen pizza!")
else:
    print("Osta toinen pizza!")