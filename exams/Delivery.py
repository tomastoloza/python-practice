import csv


def complete_location(input, output, directions):
    with open(input) as file:
        csv_reader = csv.reader(file, delimiter=",")
        first = next(csv_reader)
        output_file = open(output, "w")
        csv_writer = csv.writer(output_file, delimiter=",")
        first.append("Direction")
        csv_writer.writerow(first)
        for row in csv_reader:
            if directions.get(row[0]) is None:
                csv_writer.writerow([row[0], row[1], row[2], row[3], "Unknown direction"])
            else:
                csv_writer.writerow([row[0], row[1], row[2], row[3], directions.get(row[0])])


complete_location("../resources/clients_data", "../resources/clients_data_completed",
                  {"Ana": "Valentín Gómez 4733", "Juan": "Caseros 3033"})
