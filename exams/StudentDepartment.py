def get_remaining(students, careers, n_legacy, career):
    try:
        students[n_legacy]
    except KeyError:
        raise LegajoDesconocidoError
    try:
        careers[career]
    except KeyError:
        raise CarreraDesconocidaError
    aprobadas = [asignatura for asignatura in students[n_legacy][2] if students[n_legacy][2][asignatura][len(students[n_legacy][2][asignatura]) - 1] > 3]
    return [asignatura for asignatura in careers[career] if asignatura not in aprobadas]


class CarreraDesconocidaError(Exception):
    pass


class LegajoDesconocidoError(Exception):
    pass


alumnos = {1000: ("Ana", ["música", "pintura"], {"historia": [2, 10], "piano 1": [8], "piano 2": [2]}),
           2000: ("Juan", ["pintura"], {"historia": [6], "dibujo 1": [8], "pintura 1": [2, 7], "dibujo 2": [2]})}

carreras = {"musica": ["historia", "piano 1", "piano 2", "guitarra", "composición"],
            "pintura": ["historia", "dibujo 1", "dibujo 2", "pintura 1", "pintura 2"]}

a = get_remaining(alumnos, carreras, 1023200, "musica")
print(a)
