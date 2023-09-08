import random

def random_number():
    randomNumber = random.randint(1, 6)
    return randomNumber


generatedNumber = random_number()

while generatedNumber != 6:
    print("Numero " + str(generatedNumber) + " oli väärin.")
    generatedNumber = random_number()

print("Löysit oikean numeron: " + str(generatedNumber))