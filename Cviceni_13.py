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


# VARIANTA OD KOUCE

#ona pojmenovavala v tomhle vzorci nasobilku jako radek a cislo jako sloupec:
# for radek in range (1,5):
#     for sloupec in range (1,5):
#         print (nasobilka * cislo, end= " ")
#     print ()

# for radek in range (1,5):
#     for sloupec in range (1,8):
#         if radek == 1 or radek == 4 or sloupec == 1 or sloupec == 7:
#             print ("x", end= " ")
#         else:
#             print (" ", end= " ")
#     print ()
