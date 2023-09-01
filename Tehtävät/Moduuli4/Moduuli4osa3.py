userinput = input("Anna luku: ")
biggest = None
smallest = None

while userinput != "":
    userinput = input("Anna luku: ")
    try:
        if biggest is None or int(userinput) > int(biggest):
            biggest = userinput

        if smallest is None or int(userinput) < int(smallest):
            smallest = userinput
    except:
        print("invalid output")

print("Numeroista pienin on: " + str(smallest) + " Numeroista suurin on: " + str(biggest))