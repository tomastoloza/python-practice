def get_remaining(students, careers, n_legacy, career):
    try:
        students.get(n_legacy)
    except Exception as e:
        print(e)


alumnos = {1000: ("Ana", ["música", "pintura"], {"historia": [2, 10], "piano 1": [8], "piano 2": [2]}),
           2000: ("Juan", ["pintura"], {"historia": [6], "dibujo 1": [8], "pintura 1": [2, 7], "dibujo 2": [2]})}

carreras = {"música": ["historia", "piano 1", "piano 2", "guitarra", "composición"],
            "pintura": ["historia", "dibujo 1", "dibujo 2", "pintura 1", "pintura 2"]}

# get_remaining(alumnos, carreras, 10200, "pintura")
