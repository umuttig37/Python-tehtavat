import math

pizza = []

diameter1 = float(input("Anna ensimmäisen pitsan halkaisija senttimetreinä: "))
price1 = float(input("Anna ensimmäisen pitsan hinta: "))

diameter2 = float(input("Anna ensimmäisen pitsan halkaisija senttimetreinä: "))
price2 = float(input("Anna ensimmäisen pitsan hinta: "))


def CalculatePrice(diameter, price):
    radius = diameter / 2
    pizza_area = math.pi * radius ** 2
    pizza_price = pizza_area / price
    return pizza_price


pizza.append(CalculatePrice(diameter1, price1))
pizza.append(CalculatePrice(diameter2, price2))

if pizza[0] < pizza[1]:
    print("Toinen pizza on edullisempi.")
else:
    print("Ensimmäinen pizza on edullisempi.")