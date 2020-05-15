from datetime import datetime
from datetime import timedelta
from datetime import date

# now_plus_one = datetime.now() + timedelta(days=1)
# print(now_plus_one > datetime.now())

outer = False
while not outer:
    try:
        inputs = ["Ingrese dia", "Ingrese mes", "Ingrese año"]
        usr_date = [int(input(x + ":\n")) for x in inputs]
        usr_date = date(usr_date[2], usr_date[1], usr_date[0])
    except ValueError:
        print("Ingrese un valor correcto")
        continue
    inner = False
    while not inner:
        menu = "1. Para saber si pasó\n2. Cuantos dias\n"
        usr_input = input(menu)
        if usr_input == str(1):
            print("No pasó" if usr_date > date.today() else "Ya pasó")
        elif usr_input == str(2):
            print(usr_date.weekday())
        elif usr_input == "":
            inner = True
