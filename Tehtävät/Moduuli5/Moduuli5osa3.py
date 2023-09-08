input = int(input("Anna kokonaisluku: "))

if input > 1:
    for i in range(2, (int(input / 2) + 1)):
        if (input % i) == 0:
            print("\n" + str(input) + " ei ole alkuluku")
            break
    else:
        print("\n" + str(input) + " on alkuluku")
else:
    print("\n" + str(input) + " ei ole alkuluku")