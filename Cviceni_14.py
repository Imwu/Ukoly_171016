#CVICENI 5
cislo= int (input("Zadej cislo:"))

for pismeno in range (cislo):
    pismeno= "a"
    print (pismeno)

#CVICENI 6 A 7
cislo= int (input("Zadej cislo:"))

for cislo_radku in range (cislo):
    print ("Řádek", cislo_radku + 1) #vylepsena rovnice aby vypis nezacinal radkem 0

#CVICENI 8
zadani= int (input ("Zadej cislo:"))

for cislo in range (zadani):
    print (cislo, "na druhou je", cislo ** 2)

#CVICENI 9
zadani= int (input ("Zadej pocet krizku v radku:"))
radky9= int (input ("Zadej pocet radku:"))

for krizky in range (radky9):
    for radek in range (zadani):
        print ("X", end= " ")
    print ()

#CVICENI 10
hodnota= int (input ("Kolik radku nasobku?"))
pocet= int (input ("Jaky bude pocet nasobku na jednom radku?"))
for nasobilka in range (hodnota):
    for cislo in range (pocet):
        print (nasobilka * cislo, end= " ")
    print ()
