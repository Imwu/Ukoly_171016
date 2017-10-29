def tah (pole, cislo_policka, symbol):
    "Vrati herni pole s danym symbolem umistenym na danou pozici."

    pred= pole [:cislo_policka]
    pozice= pole [cislo_policka]
    za= pole [cislo_policka + 1:]
    print ("Chces zmenit ", pozice, "za ", symbol)

    pozice= pozice.replace (pozice, symbol)
    print (pred + pozice + za)
#KONEC DEFINICE FUNKCE

pole= "----------x---o-----"
cislo_policka= 7
symbol= "x"
tah (pole, cislo_policka, symbol)
