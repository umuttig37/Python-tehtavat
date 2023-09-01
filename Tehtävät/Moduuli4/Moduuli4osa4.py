import random
rndNumber = random.randint(1, 10)
print(str(rndNumber))
guess = int(input("Yritä arvata oikea numero 1-10 väliltä: "))


while rndNumber != guess:
    if rndNumber < guess:
        print("Liian suuri arvaus")

    if rndNumber > guess:
        print("Liian pieni arvaus")

    guess = int(input("Yritä arvata oikea numero 1-10 väliltä: "))

print("Oikein")