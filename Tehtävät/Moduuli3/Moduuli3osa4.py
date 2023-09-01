vuosiluku = int(input("Tarkistetaan, onko vuosi karkausvuosi. Anna vuosiluku: "))

if vuosiluku % 4 == 0:
    print("Vuosi on karkausvuosi.")
elif vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")