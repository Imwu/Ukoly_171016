def tah_hrace (pole, symbol):
    "Zepta se hrace, na kterou pozici chce hrat a zmeni pole."

    while True:
        cislo_policka = int (input ("Vyber pozici od 0 do 19."))
        if cislo_policka <= 19 and cislo_policka >=0 :
            print (cislo_policka)
            pozice= pole [cislo_policka]
            if pozice== "x" or pozice== "o":
                print ("Nelze provest vymenu.")
            else:
                print ("To pujde.")
                break
        else:
            print ("Spatne zadani")

    pred= pole [:cislo_policka]
    pozice= pole [cislo_policka]
    za= pole [cislo_policka + 1:]
    print ("Vymenim ", pozice, "za ", symbol)

    pozice= pozice.replace (pozice, symbol)
    print (pred + pozice + za)

#KONEC DEFINICE FUNKCE

pole= "----------x---o-----"
symbol= "x"

tah_hrace (pole, symbol)
