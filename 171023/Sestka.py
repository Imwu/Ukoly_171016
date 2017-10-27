def zjisti_pohlavi ():
    prijmeni= str (input ("Zadej sve prijmeni:"))

    print (prijmeni)
    koncovka= prijmeni [-3:]
    print (koncovka)

    if koncovka== "ova":
        print ("Zena")
    else:
        print ("Muz")

zjisti_pohlavi ()
