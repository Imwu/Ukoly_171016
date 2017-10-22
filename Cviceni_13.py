for radek in range (5):
    if radek== 0 or radek== 4:
        for znak in range (6):
            print ("X", end= " ")
        print ()
    else:
        for znak in range (6):
            if znak== 0 or znak==5:
                print ("X", end= " ")
            else:
                print (" ", end= " ")
        print ()
