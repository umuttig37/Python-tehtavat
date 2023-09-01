userNameInput = input("Anna käyttäjätunnus: ")
passwordInput = input("Anna salasana: ")


i = 0
username = "python"
password = "rules"

while userNameInput != username or passwordInput != password:
    print("Väärät kirjautumisteidot, anna tiedot uudelleen")
    i += 1
    if i == 5:
        print("Pääsy evätty")
        break

    userNameInput = input("Anna käyttäjätunnus: ")
    passwordInput = input("Anna salasana: ")


    if userNameInput == username and passwordInput == password:
        print("Tervetuloa")
        break