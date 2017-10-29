vstup = "xoxoxoxoxoxoxoxoxoxo"

def vyhodnot (vstup):

    if ("xxx" in vstup):
        print ("x") #Vyhral hrac s krizky
    elif ("ooo" in vstup):
        print ("o") #Vyhral hrac s kolecky
    elif ("-" not in vstup):
        print ("!") #Remiza
    else:
        print ("-") #Hra pokracuje

vyhodnot (vstup)
