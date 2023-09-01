sex = input("Anna biologinen sukupuolesi: ")
hemog = int(input("Anna sinun hemoglobiiniarvo g/l: "))


if sex == "nainen":
    if hemog < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemog >= 117 and hemog <= 175:
        print("Hemoglobiiniarvosi on normaali")
    else:
        print("Hemoglobiiniarvosi on korkea.")

if sex == "mies":
    if hemog < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemog >= 134 and hemog <= 195:
        print("Hemoglobiiniarvosi on normaali")
    else:
        print("Hemoglobiiniarvosi on korkea.")