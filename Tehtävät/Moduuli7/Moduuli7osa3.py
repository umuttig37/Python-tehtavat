dict = {}

while True:
    print("Valinta 1: Lentokentän tallentaminen")
    print("Valinta 2: Lentokentän etsiminen")
    print("Valinta 3: Lopeta ohjelma")
    valinta = int(input("Anna valinta 1-3 "))

    if valinta == 1:
        icao = input("Anna lentokentän ICAO-koodi: ")
        lentokentanNimi = input("Anna lentokentän nimi: ")
        dict[icao] = lentokentanNimi
        print("Lentokentän nimi tallennettu.")

    if valinta == 2:
        icao_koodi = input("Anna ICAO-koodi: ")

        if icao_koodi in dict.keys():
            print(dict[icao_koodi])
        else:
            print("Tällä ICAO-koodilla ei löydy lentokenttää.")

    if valinta == 3:
        break
