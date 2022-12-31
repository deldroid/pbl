import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

# defing list with database files
files = [
    '2015/Zdarzenia.csv',
    '2016/Zdarzenia.csv',
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
    data = data_dict["Warunki atmosferyczne"][x] 

    if data in result_dict.keys():
        result_dict[data] += 1
    else:
        result_dict[data] = 1


result_dict = dict(sorted(result_dict.items(), key=lambda item: item[1]))
result_dict = dict(list(result_dict.items())[-5:])

print(result_dict)


def lighting(): #translation for lighting
    result_dict['daylight'] = result_dict.pop(f"{'światło dzienne'.capitalize()}")
    result_dict['night - the road is lit'] = result_dict.pop(f"{'noc - droga oświetlona'.capitalize()}")
    result_dict['night - the road is unlit'] = result_dict.pop(f"{'noc - droga nieoświetlona'.capitalize()}")
    result_dict['sunrise'] = result_dict.pop(f"\"{'świt, zmrok'.capitalize()}\"")


def surface(): #translation for surface
    result_dict['dry'] = result_dict.pop("Sucha")
    result_dict['wet'] = result_dict.pop("Mokra")
    result_dict['Icing, snowing'] = result_dict.pop("\"Oblodzenie, zaśnieżenie\"")
    result_dict['Wet; icing, snowing'] = result_dict.pop('\"Mokra; Oblodzenie, zaśnieżenie\"')
    result_dict['Holes, bumps'] = result_dict.pop('\"Dziury, wyboje\"')


def weather(): #translation for weather
    result_dict['good weather'] = result_dict.pop('Dobre warunki atmosferyczne')
    result_dict['cloudy'] = result_dict.pop('Pochmurno')
    result_dict['snowfall, hail'] = result_dict.pop("\"Opady śniegu, gradu\"")
    result_dict['rain'] = result_dict.pop("Opady deszczu")
    result_dict['dazzling sun'] = result_dict.pop("oślepiające słońce".capitalize())
    

#surface()
#lighting()
weather()

objects = list(result_dict.keys())
y_pos = np.arange(len(objects))
performance = list(result_dict.values())

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Weather')

plt.show()
