from random import randrange

def vymena_hracu (symbol):
    if symbol== "x":
        symbol= "o"
        return symbol
    else:
        symbol= "x"
        return symbol
#KONEC DEFINICE FUNKCE

def tah (pole, cislo_policka, symbol):
    "Vrati herni pole s danym symbolem umistenym na danou pozici."

    pred= pole [:cislo_policka]
    pozice= pole [cislo_policka]
    za= pole [cislo_policka + 1:]
    print ("Chces zmenit", pozice, "za", symbol)

    pozice= pozice.replace (pozice, symbol)
    nove_pole= pred + pozice + za
    print (pred + pozice + za)
    return nove_pole
#KONEC DEFINICE FUNKCE

def tah_hrace (pole, symbol):
    "Zepta se hrace, na kterou pozici chce hrat a zmeni pole."

    while True:
        cislo_policka = int (input ("Vyber pozici od 0 do 19."))
        if cislo_policka <= 19 and cislo_policka >=0 :
            print (cislo_policka)
            pozice= pole [cislo_policka]
            if pozice== "x" or pozice== "o":
                print ("Nelze provest vymenu, vyber jine cislo.")
            else:
                break
        else:
            print ("Spatne zadani")

    nove_pole= tah (pole, cislo_policka, symbol)
    return nove_pole
#KONEC DEFINICE FUNKCE

def tah_pocitace (pole):
    "Vrati herni pole se zaznamenanym tahem pocitace."
    symbol= "o"
    while True:
        cislo_policka = randrange (0,20)
        print (cislo_policka)
        pozice= pole [cislo_policka]
        if pozice == "x" or pozice== "o":
            print ("Pozice obsazena, generuji nove cislo.")
        else:
            print ("Provadim tah na pozici ", cislo_policka)
            break

    nove_pole= tah(pole, cislo_policka, symbol)
    return nove_pole
#KONEC DEFINICE FUNKCE

def vyhodnot (pole):
    if ("xxx" in pole):
        print ("Konec hry, vyhral clovek.")
        return False
    elif ("ooo" in pole):
        print ("Konec hry, vyhral pocitac")
        return False
    elif ("-" not in pole):
        print ("Konec hry, remiza.")
        return False
    else:
        print ("Hra pokracuje.")
        return True
#KONEC DEFINICE FUNKCE

def piskvorky1d ():
    pole= "--------------------"
    symbol= "x"
    hra= True
    while hra== True:
        if symbol== "x":
            pole= tah_hrace (pole, symbol)
        else:
            pole= tah_pocitace (pole)
        hra= vyhodnot (pole)
        symbol= vymena_hracu (symbol)
#KONEC DEFINICE FUNKCE

piskvorky1d ()
