userInput = input("Anna numero: ")

numbers = []

while userInput != "":
    numbers.append(float(userInput))
    userInput = input("Anna numero: ")


def listSum(array):
    sum = 0
    for number in array:
        sum += number

    return print(sum)


listSum(numbers)