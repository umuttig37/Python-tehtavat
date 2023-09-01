leiviskälkm = float(input("Anna leiviskät: "))
naulalkm = float(input("Anna naulat: "))
luotilkm = float(input("Anna luodit: "))


luoditg = float(13.3 * luotilkm)
naulatg = float(32 * 13.3 * naulalkm)
leiviskätg = float((32 * 13.3 * 20)*leiviskälkm)


massa = float(luoditg+naulatg+leiviskätg)
massag = massa % 1000
massakg = int (massa / 1000)

print(f"Massa nykymittojen mukaan: \n {massakg} kilogrammaa ja  {massag:.2f} grammaa.")



