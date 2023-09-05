list = []

while True:
    numerot = input("Anna luku: ")
    if numerot.isnumeric():
        numerot = int(numerot)
    if numerot == "":
        break
    if type(numerot) == str:
        continue
    list.append(numerot)

list.sort()

print(list[-5:])
