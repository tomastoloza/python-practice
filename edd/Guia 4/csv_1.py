import csv


def get_company_with_most_proyects():
    with open("1 - empresas-ejecutoras-proyectos.csv", "r") as file:
        reader = csv.reader(file)
        companies = {}
        next(reader)
        for row in reader:
            companies.setdefault(row[1], set())
            companies[row[1]].add(row[0])
    maxi = 0
    maxi_company = ""
    for company in companies.keys():
        if len(companies[company]) > maxi:
            maxi = len(companies[company])
            maxi_company = company
    print(maxi_company)


def get_province_with_most_companies():
    with open("1 - empresas-ejecutoras-proyectos.csv", "r") as file:
        reader = csv.reader(file)
        companies = {}
        next(reader)
        for row in reader:
            companies.setdefault(row[5], set())
            companies[row[5]].add(row[1])
        maxi = 0
        maxi_company = ""
        for company in companies.keys():
            if len(companies[company]) > maxi:
                maxi = len(companies[company])
                maxi_company = company
        print(maxi_company)


def get_province_with_most_proyects():
    with open("1 - empresas-ejecutoras-proyectos.csv", "r") as file:
        reader = csv.reader(file)
        companies = {}
        next(reader)
        for row in reader:
            companies.setdefault(row[5], set())
            companies[row[5]].add(row[0])
        maxi = 0
        maxi_company = ""
        for company in companies.keys():
            if len(companies[company]) > maxi:
                maxi = len(companies[company])
                maxi_company = company
        print(maxi_company)


if __name__ == '__main__':
    # get_company_with_most_proyects()
    # get_province_with_most_companies()
    get_province_with_most_proyects()