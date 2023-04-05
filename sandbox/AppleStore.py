file_path = 'C:\Misc\AppleStore.csv'
opened_file = open(file_path, encoding="utf8")
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

import pandas as pd

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}
for row in apps_data[1:]:
    c_rating = row[11]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
# print(content_ratings)

content_data = {}

for i in apps_data[1:]:
    c_column = float(i[3])
    if c_column in content_data:
        content_data[c_column] += 1
    else:
        content_data[c_column] = 1
#print(content_data)
print(min(content_data)/1000000)
print(max(content_data)/1000000)
print(len(apps_data[1:]))

data_sizes = {'0 - 10 MB': 0, '10 - 50 MB': 0, '50 - 100 MB': 0,
                    '100 - 500 MB': 0, '500 - 1000 MB': 0, '1 GB - 3 GB': 0, '3 GB +': 0}

for row in apps_data[1:]:
    data_size = float(row[3])

    if data_size <= 10000000:
        data_sizes['0 - 10 MB'] += 1

    elif 10000000 < data_size <= 50000000:
        data_sizes['10 - 50 MB'] += 1

    elif 50000000 < data_size <= 100000000:
        data_sizes['50 - 100 MB'] += 1

    elif 100000000 < data_size <= 500000000:
        data_sizes['100 - 500 MB'] += 1

    elif 500000000 < data_size <= 1000000000:
        data_sizes['500 - 1000 MB'] += 1

    elif 1000000000 < data_size <= 3000000000:
        data_sizes['1 GB - 3 GB'] += 1           

    elif data_size > 3000000000:
        data_sizes['3 GB +'] += 1

print(data_sizes)

unique_values = set(content_data)
#print(unique_values)

# for n in content_data:
# print(n)

total_number_of_apps = len(apps_data[1:])
c_ratings_proportions = {}

for key in content_ratings:
    proportion = (content_ratings[key] / total_number_of_apps)  *100   
    c_ratings_proportions[key] = proportion

# print(c_ratings_proportions)
# print(content_ratings)    
