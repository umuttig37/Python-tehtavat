from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<int:numero>')
def alkuluku(numero):
    if numero > 1:
        for x in range(2, int(numero/2) + 1):
            if numero % x == 0:
                isalkuluku = False
                vastaus = {
                "number" : numero,
                "prime" : isalkuluku
                }
                return jsonify(vastaus)

        isalkuluku = True
        vastaus = {
        "number" : numero,
        "prime" : isalkuluku
        }
        return jsonify(vastaus)
    isalkuluku = True
    vastaus = {
    "number" : numero,
    "prime" : isalkuluku
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(use_reloader = True, host='127.0.0.1', port=3000)