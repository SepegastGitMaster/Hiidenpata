def parilliset(annetut_numerot):
    lista = []
    for i in annetut_numerot:
        if i % 2 == 0:
            lista.append(i)
    return lista

#testaus
annetut_numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Annetut numerot olivat:",annetut_numerot)
print("Numeroista parillisia olivat:",parilliset(annetut_numerot))
