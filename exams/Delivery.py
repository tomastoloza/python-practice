import csv


def complete_location(input, output, directions):
    with open(input, 'r') as file, open(output, 'w+') as file_writer:
        writer = csv.writer(file_writer)
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            completed_row = row[:]
            try:
                completed_row.append(directions[completed_row[0]])
            except KeyError:
                completed_row.append("Direccion desconocida")
            writer.writerow(completed_row)


complete_location("../resources/clients_data", "../resources/clients_data_completed",
                  {"Ana": "Valentín Gómez 4733", "Juan": "Caseros 3033"})
