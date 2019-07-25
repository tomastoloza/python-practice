def get_number():
    while True:
        try:
            entered = int(input("Tell me a number and I will tell you if it is even or odd\n"))
            if entered % 2 == 0:
                print(str(entered) + " is even\n")
                if entered % 6 == 0:
                    print(str(entered) + " is also multiple of 6\n")

            else:
                print(str(entered) + " is odd\n")
            break
        except ValueError:
            print("That is not a number")


get_number()
