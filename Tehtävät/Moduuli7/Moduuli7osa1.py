import string

vuodenajat = {
    "kevät": (3, 4, 5),
    "kesä": (6, 7, 8),
    "syksy": (9, 10, 11),
    "talvi": (12, 1, 2)
}


kuukausi_numero = int(input("Syötä kuukauden numero (1-12): "))
vuodenaika = ""
for kausi, numerot in vuodenajat.items():
    if kuukausi_numero in numerot:
        vuodenaika = kausi
        break


if vuodenaika == "":
    print("Anna numero 1-12.")

else:
    print(kausi)