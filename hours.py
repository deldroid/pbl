import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

# defing list with database files
files = [
    '2017/Zdarzenia.csv',
    '2018/Zdarzenia.csv',
    '2020/Zdarzenia.csv',
    '2021/Zdarzenia.csv'
]

matrix4x24 = []

for file_name in files:
    file = open(file_name, encoding='utf-16').read() # reading file in utf 16 encoding to work with polish symbols

    rows = file.split('\n')[0].split('	') # headers

    # creating dictionary with empty list for each header as key
    data_dict = {}
    for row in rows:
        data_dict[row] = []

    data_rows = file.split('\n')[1:] # rows with data

    # writing rows with data to data_dict in useful format. data_dict variable can be used for other purposes.
    for row in data_rows:
        data_row = row.split('	')

        for i in range(len(data_row)):
            data_dict[rows[i]].append(data_row[i])

    # defining order
    hours = {
        "03": 0,
        "04": 0,
        "05": 0,
        "06": 0,
        "07": 0,
        "08": 0,
        "09": 0,
        "10": 0,
        "11": 0,
        "12": 0,
        "13": 0,
        "14": 0,
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 0,
        "21": 0,
        "22": 0,
        "23": 0}

    for time in data_dict['Data zdarzenia']:
        time = time.split(" ")[1].split(":")[0]

        if time in hours:
            hours[time] += 1
        else:
            hours[time] = 1

    matrix4x24.append(list(hours.values()))

# reversing matrix
matrix24x4 = []
for i in range(24):
    list4 = []
    for x in range(4):
        list4.append(matrix4x24[x][i])
    matrix24x4.append(list4)

# calculating min, max and average
average = []
list_min, list_max = [], []

for element in matrix24x4: 
    average.append(sum(element) / 4)
    list_min.append(min(element))
    list_max.append(max(element))

plt.plot(hours.keys(), average)
plt.fill_between(hours.keys(), list_min, list_max, alpha=.5)
plt.show()


objects = ('2017', '2018', '2020', '2021')
y_pos = [1, 2, 3, 4]

# counting total for each year
total = []
for i in range(4):
    total.append(sum(matrix4x24[i]))

plt.bar(y_pos, total, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.show()
