list = []

while True:
    input = input("Anna numero: ")
    if input == "":
        break
    list.append(float(input))

list.sort(reverse=True)

print("Viisi suurinta numeroa ovat: \n")

for i in range(5):
    print(list[i])