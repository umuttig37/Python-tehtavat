import random

maxNoppa = int(input("Anna nopan maksimisilmäluku: "))


def randomLuku(maxnumber):
    randomLuku = random.randint(1, maxnumber)
    return randomLuku


generatedLuku = randomLuku(maxNoppa)

while generatedLuku != maxNoppa:
    print("Numero " + str(generatedLuku) + " oli väärin.")
    generatedLuku = randomLuku(maxNoppa)

print("Nopan maksimisilmäluku: " + str(generatedLuku))