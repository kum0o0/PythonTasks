import json
import csv

def export_to_csv(name):

    with open(name, 'r') as json_file:
        data = json.load(json_file)
        keys = list(data.keys())
        names = data[keys[0]]

    with open(f'{keys[0]}.csv','w') as csv_file:
        fieldnames = names[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for name in names:
            writer.writerow(name)

export_to_csv("Sample-employee-JSON-data.json")
export_to_csv("Sample-JSON-file-with-multiple-records.json")


