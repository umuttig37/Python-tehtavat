import math

gallons = input("Anna bensiinin määrä nestegallonoina: ")


def ConvertGallonToLiter(gallonamount):
    return print(gallonamount * 3.785)


while gallons != "":
    ConvertGallonToLiter(float(gallons))
    gallons = input("Anna bensiinin määrä nestegallonoina: ")