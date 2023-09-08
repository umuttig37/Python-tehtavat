import random

lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))

for x in range(lukumaara):
    print(random.randint(0, 6))


