input = input("Anna numero: ")

numbers = []

while input != "":
    numbers.append(float(input))
    input = input("Anna numero: ")


def listEven(array):
    print(array)
    print("\n")

    for oddNumber in array:
        if oddNumber % 2 != 0:
            array.remove(oddNumber)
    return print(array)


listEven(numbers)