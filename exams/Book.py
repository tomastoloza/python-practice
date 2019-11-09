import csv


def complete_book(csv_entrada, csv_salida, dictionary):
    with open(csv_entrada, 'r') as file_read, open(csv_salida, 'w+') as file_write:
        reader = csv.reader(file_read, delimiter=",")
        writer = csv.writer(file_write)
        next(reader)
        for row in reader:
            completed_row = row[:]
            try:
                completed_row.append(dictionary[row[2]][0])
                completed_row.append(dictionary[row[2]][1])
            except KeyError:
                completed_row.append("Libro desconocido")
                completed_row.append("Autor desconocido")
            writer.writerow(completed_row)


falopa = {'20': ("Mining the Social Web", "M. A. Russell"),
          '5': (
              "Data structures and problemsolving using Java",
              "M. A. Weiss")}
complete_book("../resources/solicitud.csv", "../resources/books.csv", falopa)
