import mysql.connector
from flask import Flask, Response

dbconn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='test1',
    autocommit=True
)

app = Flask(__name__)
@app.route("/kentta/<icao>")
def kentta(icao):
    icao = str(icao)
    sql = "SELECT name, municipality FROM airport WHERE ident='" + icao + "'"
    kursori = dbconn.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    response = {}
    if kursori.rowcount > 0:
        for rivi in tulos:
            response = {"ICAO": icao,
                        "Name": rivi[0],
                        "Municipality": rivi[1]}

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)