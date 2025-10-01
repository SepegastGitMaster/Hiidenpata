tuuma = float(input("Anna tuumat: "))
while tuuma >= 0:
    sentit = tuuma * 2.54
    print(f"On sentteinä {sentit:.2f}")
    tuuma = float(input("Anna tuumat: "))
print ("Syötit negatiivisen arvon - tuumamuunnin lopetti toimintansa")