import numpy as np
import matplotlib.pyplot as plt
import datetime
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


result_dict = {}

for x in range(200000):
    data = data_dict["Data zdarzenia"][x].split(" ")[0].split("-")

    today = datetime.datetime(int(data[0]), int(data[1]), int(data[2]))
    day = today.weekday()

    if day in result_dict.keys():
        result_dict[day] += 1
    else:
        result_dict[day] = 1

print(result_dict)

result_dict["monday"] = result_dict.pop(0)
result_dict["tuesday"] = result_dict.pop(1)
result_dict["wednesday"] = result_dict.pop(2)
result_dict["thursday"] = result_dict.pop(3)
result_dict["friday"] = result_dict.pop(4)
result_dict["saturday"] = result_dict.pop(5)
result_dict["sunday"] = result_dict.pop(6)

objects = list(result_dict.keys())
y_pos = np.arange(len(objects))
performance = list(result_dict.values())

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('weekday')

plt.show()
