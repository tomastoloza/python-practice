import csv


def get_region_with_more_revenue():
    with open("2 - proyectos-cyt.csv", "r") as file:
        reader = csv.reader(file)
        region = {}
        next(reader)
        for row in reader:
            region.setdefault(row[9], set())
            region[row[9]].add(row[0])
        print(region)


if __name__ == '__main__':
    get_region_with_more_revenue()
