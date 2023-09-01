userinput = input("Syötä laivan hyttiluokka: ")

if userinput == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif userinput == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif userinput == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif userinput == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")