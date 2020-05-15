
def hex_to_dec():
    list_hex = ["FF","DDE", "14916", "FC4", "AA21"]
    for i in list_hex:
         print(i + " = "+ str(int(i,16)))

def dec_to_hext():
    list_dec = [(("a."), (127)),    (("b."), (2901)),    (("c."), (109720)),    (("d."), (683)),    (("e."), (1133))]
    for i in list_dec:
        print(i[0]+ " " + str(i[1])+ " = " + str(hex(i[1]).split("x")[1].upper()))

if __name__ == '__main__':
    dec_to_hext()


# TODO: regex autom