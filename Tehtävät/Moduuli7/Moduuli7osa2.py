dict = {}
list = []
counter = 0
while True:
    nimi = input("Anna nimi ")
    if nimi == "":
        break
    dict[str(counter)] = nimi
    counter += 1

print("nimi on jo annettu" if len(set(dict.values())) != len(dict.values()) else "uusi nimi.")

