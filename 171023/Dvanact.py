from random import randrange
def tah (pole, cislo_policka, symbol):
    "Vrati herni pole s danym symbolem umistenym na danou pozici."

    pred= pole [:cislo_policka]
    pozice= pole [cislo_policka]
    za= pole [cislo_policka + 1:]
    print ("Chces zmenit ", pozice, "za ", symbol)

    pozice= pozice.replace (pozice, symbol)
    nove_pole= pred + pozice + za
    print (pred + pozice + za)
    return nove_pole

#KONEC DEFINICE FUNKCE

def tah_pocitace (pole):
    "Vrati herni pole se zaznamenanym tahem pocitace."
    while True:
        cislo_policka = randrange (0,20)
        print (cislo_policka)
        pozice= pole [cislo_policka]
        if pozice == "x" or pozice== "o":
            print ("Pozice obsazena, generuji nove cislo.")
        else:
            print ("Provadim tah na pozici ", cislo_policka)
            break

    tah(pole, cislo_policka, symbol)

pole= "---xoxo-x-xo-o----xo"
symbol= "o"

tah_pocitace (pole)
