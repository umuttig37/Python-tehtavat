luku = int(input("Anna kokonaisluku: "))
isnotalkuluku = False
for x in range(luku):
    if x == 0 or x == luku or  x == 1:
        continue

    if luku % 1 == 0 and luku % luku == 0 and luku % x == 0:
            isnotalkuluku = True



if isnotalkuluku == True:
    print("not alkuluku!")