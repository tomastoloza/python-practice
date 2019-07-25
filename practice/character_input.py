def get_age():
    while True:
        try:
            return str(int(input("Tell me your age\n")))
        except ValueError:
            print("THAT'S NOT A NUMBER")


def get_name_and_age():
    print("Your name is " + getName().capitalize() + " and you are " + get_age() + " years old")


def getName():
    return input("Tell me your name\n")
