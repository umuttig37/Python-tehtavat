import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinenNopeus = 0
        self.kuljettuMatka = 0

    def ShowSpecs(self):
        print("Rekisteritunnus: ", self.rekisteritunnus)
        print("Huippunopeus: ", self.huippunopeus)
        print("Hetkellinen Nopeus: ", self.hetkellinenNopeus)
        print("Kuljettu matka: ", self.kuljettuMatka)
    def kiihdytä(self, nopeus):
        self.hetkellinenNopeus += nopeus
        if self.hetkellinenNopeus > self.huippunopeus:
            self.hetkellinenNopeus = self.huippunopeus
        if self.hetkellinenNopeus < 0:
            self.hetkellinenNopeus = 0
        print("nopeus on nyt: ", self.hetkellinenNopeus)

    def kulje(self, tuntimäärä):
        self.kuljettuMatka += self.hetkellinenNopeus * tuntimäärä
        print("Kuljettu matka: ", self.kuljettuMatka)


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self, tunti):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-15, 15))
            auto.kulje(tunti)

    def tulosta_tilanne(self):
        print("Rekisteritunnus\tNykyinen nopeus (km/h)\tKuljettu matka (km)")
        for auto in self.autot:
            if auto.kuljettuMatka > 8000:
                print(f"{auto.rekisteritunnus:15} {auto.hetkellinenNopeus:15} {auto.kuljettuMatka:15} Voittaja!")
            else:
                print(f"{auto.rekisteritunnus:15} {auto.hetkellinenNopeus:15} {auto.kuljettuMatka:15}")



    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettuMatka >= self.pituus:
                return True
        return False


class Sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekkari, huippunopeus)


class BensaAuto(Auto):
    def __init__(self, rekkari, huippunopeus, tankkikoko):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.tankkikoko = tankkikoko
        super().__init__(rekkari, huippunopeus)


"""
#osa1
auto = Auto("abc-123", 143 )
auto.ShowSpecs()

#osa2
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)

#osa3
auto.kiihdytä(60)
auto.kulje(1.5)

#osa4
autolista = []
abcplussable = 0
for x in range(10):
    abcplussable += 1
    huippunopeus = random.randint(100,200)
    autolista.append(Auto("ABC-" + str(abcplussable), huippunopeus))

onkokuljettu = False
while(onkokuljettu == False):
    for x in range(len(autolista)):
        if onkokuljettu == False:
            autolista[x].kiihdytä(random.randint(-10, 15))
            autolista[x].kulje(1)
            if autolista[x].kuljettuMatka > 10000:
                print("Auto" + str(autolista[x].rekisteritunnus), "Voitti!")
                onkokuljettu = True
            print("auto " + str(autolista[x].rekisteritunnus), autolista[x].kuljettuMatka)

#Moduuli10osa4 
autot = []
abcplussable = 0
for x in range(10):
    abcplussable += 1
    huippunopeus = random.randint(100,200)
    autot.append(Auto("ABC-" + str(abcplussable), huippunopeus))


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu(1)
    tunti += 1
    if tunti % 10 == 0:
        print(f"Tunti {tunti} tilanne:")
        kilpailu.tulosta_tilanne()

print("Kilpailu päättyi!")
kilpailu.tulosta_tilanne()
"""

sähköauto = Sähköauto("SHK-123", 180, 31.31)
bensaAuto = BensaAuto("PWR-123", 300, 60.01)
sähköauto.kiihdytä(100)
bensaAuto.kiihdytä(300)
sähköauto.kulje(3)
bensaAuto.kulje(2)
