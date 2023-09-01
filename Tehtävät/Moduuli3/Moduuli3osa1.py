kuhanpituus = int(input("Anna kuhan pituus senttimetreinä: "))

if kuhanpituus < 37:
    print("Kuha on "+str(37-kuhanpituus)+" cm liian lyhyt. Laske kuha takaisin järveen.")
else:
    print("Pyydystit "+str(kuhanpituus)+" cm pituisen kuhan.")