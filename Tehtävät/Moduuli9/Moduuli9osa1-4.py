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

