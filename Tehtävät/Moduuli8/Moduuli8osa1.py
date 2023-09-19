import mysql.connector
def haeLentokenttaICAOnimenAvulla(ICAO):
    sql = "SELECT name, iso_region FROM airport"
    sql += " WHERE ident='" + ICAO + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi)
    else:
        print("Tällä ICAO-koodilla ei löydy lentokenttää")





yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'airport',
    user = 'root',
    password = 'Salasana1',
    autocommit = True
)

icao = input("Anna ICAO koodi: ")
haeLentokenttaICAOnimenAvulla(icao)