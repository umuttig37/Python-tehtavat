class Hissi:
    def __init__(self, hissi = 0):
        self.hissi = hissi

    def kerros_ylos(self):
        self.hissi += 1
        print(f"Ollaan kerroksessa {self.hissi}")

    def kerros_alas(self):
        self.hissi -= 1
        print(f"Ollaan kerroksessa {self.hissi}")

    def siirry_kerrokseen(self, luku):
        while self.hissi != luku:
            if self.hissi < luku:
                self.kerros_ylos()
            if self.hissi > luku:
                self.kerros_alas()

class Talo:
    def __init__(self, alinKerros, ylinKerros, hissienMaaara):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.hissienMaara = hissienMaaara
        self.hissit = [Hissi() for _ in range(self.hissienMaara)]

    def aja_hissiä(self, hissiNro, kohdekerros):
        if 0 <= kohdekerros < len(self.hissit):
            hissi = self.hissit[hissiNro]
            hissi.siirry_kerrokseen(kohdekerros)
            print(f"hissi nro {hissiNro}")

    def palohälytys(self):
        print("palohälytys!")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(0)


hissi = Hissi()

hissi.siirry_kerrokseen(7)
hissi.kerros_ylos()


talo = Talo(0, 7, 5)

talo.aja_hissiä(4, 4)
talo.palohälytys()
