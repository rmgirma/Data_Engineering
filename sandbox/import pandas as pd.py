import csv
from datetime import datetime, timedelta

def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding="utf8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
        file.close()
    return data


file_path = r'C:\Misc\AppleStore.csv'
apps_data = read_csv(file_path)

content_data = {}

for i in apps_data[1:]:
    c_column = i[11]
    if c_column in content_data:
        content_data[c_column] += 1
    else:
        content_data[c_column] = 1
print(content_data)
tot = content_data['4+'] + content_data['9+'] + content_data['12+'] + content_data['17+']
print(tot)
print(len(apps_data[1:]))

unique_values = set(content_data)
print(unique_values)

