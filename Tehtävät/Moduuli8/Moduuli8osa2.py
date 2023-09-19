import mysql.connector
def LaskeLentoKenttiäPerCountry(country):
    sql = "SELECT type, count(*) AS amount FROM airport WHERE iso_country = '" + country + "' GROUP BY type"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print("Lentokenttiä " + rivi[0] + " on " + str(rivi[1]) + " Kappaletta")
        return








yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'airport',
    user = 'root',
    password = 'Salasana1',
    autocommit = True
)

kaupunki = input("Anna maan nimi: ")
LaskeLentoKenttiäPerCountry(kaupunki)
