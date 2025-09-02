leivis = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))
naulat = naula + 20 * leivis
luodit = luoti + 32 * naulat
grammat = luodit * 13.3
kg = int(grammat // 1000)
gr = int(grammat % 1000)
print("Massa nykymittojen mukaan: ",kg," kilogrammaa ja ",gr," grammaa.")
