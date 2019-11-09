import csv


def get_more_time_activity(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        more_time = {}
        activities = {}
        for row in reader:
            activities.setdefault(row[0], {})
            activities[row[0]].setdefault(row[2], 0)
            activities[row[0]][row[2]] += int(row[3])

        for key in activities:
            print(activities[key])
            max = 0
            activity = ""
            for inner in activities[key]:
                if activities[key][inner] > max:
                    max = activities[key][inner]
                    activity = inner
            print(max, activity)


get_more_time_activity("entrada.csv")
