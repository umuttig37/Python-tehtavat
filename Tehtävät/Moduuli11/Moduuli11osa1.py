class Julkaisu:
    def __init__(self, julkaisu):
        self.julkaisu = julkaisu

    def tulosta_tiedot(self):
        print("julkaisu:", self.julkaisu)


class Kirja(Julkaisu):
    def __init__(self, kirja, kirjoittaja, sivumäärä):
        self.kirja = kirja
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(kirja)


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Kirjoittaja:", self.kirjoittaja, "  Sivumäärä:", self.sivumäärä)

class Lehti(Julkaisu):
    def __init__(self, lehti, päätoimittaja):
        self.lehti = lehti
        self.päätoimittaja = päätoimittaja
        super().__init__(lehti)


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("päätoimittaja:", self.päätoimittaja)



autoKirja = Kirja("Bmw Kirja", "Umut", 60)
autoLehti = Lehti("Mersu lehti", "Karl Benz")
autoKirja.tulosta_tiedot()
autoLehti.tulosta_tiedot()