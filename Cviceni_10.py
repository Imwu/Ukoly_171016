#tabulka male nasobilky - nasobim radek sloupcem = kdyz si to napises do tabulky tak to dava smysl
#je smysluplnejsi pojmenovat promenne radek a sloupec protoze vypisujes tabulku
    # je to i srozumitelnejsi pro nekoho, kdo to po tobe cte

for nasobilka in range (5):
    for cislo in range (5):
        print (nasobilka * cislo, end= " ")
    print ()

#Range muzes napsat taky v teto podobe - range (1, 5)
    # v tu chvili ti range bude pocitat od cisla 1 do cisla 5, ale petku uz to nevypise
    # je to dalsi zpusob jak se zbavit nuly
