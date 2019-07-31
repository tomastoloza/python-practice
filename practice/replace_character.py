with open("string.txt") as file:
    asd = file.read().replace("“", "\"")
    ase = asd.replace("”", "\"")

    print("\n" + ase + "\n")
