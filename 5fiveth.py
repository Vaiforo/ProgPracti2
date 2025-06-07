import pandas as pd

"""
1) Создайте датафрейм с следующими данными:
Name Age Sex
Strom, Mrs. Wilhelm (Elna Matilda Persson) 29 female
Navratil, Mr. Michel ("Louis M Hoffman") 36,5 male
Minahan, Miss. Daisy E 33 female
"""
print("\n\t\tЗадание 1\n")

data = {
    'Name': [
        'Strom, Mrs. Wilhelm (Elna Matilda Persson)',
        'Navratil, Mr. Michel ("Louis M Hoffman")',
        'Minahan, Miss. Daisy E'
    ],
    'Age': [29, 36.5, 33],
    'Sex': ['female', 'male', 'female']
}

dataframe1 = pd.DataFrame(data)
dataframe1.columns = dataframe1.columns.str.lower()
print(dataframe1)

"""
2) Загрузите данные из файла:
https://drive.google.com/file/d/16gikf9vvMLyldkdHtoDYrPDbqTHP1BxG/view?usp=share_link
"""
print("\n\t\tЗадание 2\n")

dataframe2 = pd.read_csv('titanic_csv.csv', encoding='utf-8', sep=';')
dataframe2.columns = dataframe2.columns.str.lower()
print(dataframe2)

"""
3) Загрузите напрямую данные по ссылке: https://clck.ru/3FNueV (read_csv).
"""
print("\n\t\tЗадание 3\n")

dataframe3 = pd.read_csv(
    'https://gist.githubusercontent.com/zaryanezrya/8b4ef51c707cb16d5e88a44dc00a1bb2/raw/41230f49c6268e072dbf102672f670be256922ab/gistfile1.txt',
    encoding='utf-8', sep=',')
print(dataframe3)

"""
4) Объедините датафреймы из п. 2, 3 в один датафрейм, удалите дубликаты строк.
"""
print("\n\t\tЗадание 4\n")

dataframe = pd.concat([dataframe2, dataframe3], ignore_index=True)
dataframe.drop_duplicates(inplace=True)
print(dataframe)

"""
5) Задайте в качестве индекса датафрейма id пассажира.
Отсортируйте по индексу (sort_values).
"""
print("\n\t\tЗадание 5\n")

dataframe.set_index('passengerid', inplace=True)
dataframe.sort_values(by='passengerid', inplace=True)
print(dataframe)

"""
6) Отобразите информацию и базовую статистику по датафрейму (info, describe)
"""
print("\n\t\tЗадание 6\n")

print(dataframe.info())
print(dataframe.describe())

"""
7) Поменяйте местами нулевую по порядку строку с элементом с индексом 2 (loc, iloc).
"""
print("\n\t\tЗадание 7\n")

dataframe.iloc[0], dataframe.loc[2] = dataframe.loc[2].values, dataframe.iloc[0].values
print(dataframe)

"""
8) В столбце Sex замените female/male на f/m (map).
"""
print("\n\t\tЗадание 8\n")

dataframe['sex'] = dataframe['sex'].map({'female': 'f', 'male': 'm'})
print(dataframe)

"""
9) Найдите билеты по которым плыло 6 и более человек, отобразите список людей. (groupby, count).
"""
print("\n\t\tЗадание 9\n")

tickets_groups = dataframe.groupby('ticket').size().reset_index(name='сount')
tickets_with_count_more_5 = tickets_groups[tickets_groups['сount'] >= 6]['ticket'].tolist()
result = dataframe[dataframe['ticket'].isin(tickets_with_count_more_5)]
sorted_result = result.sort_values(by='ticket')

print("Список людей по билетам с количеством пассажиров 6 и более:")
print(sorted_result[['name', 'ticket']])

"""
10) Найдите людей, которые плыли в одной каюте с людьми из датафрейма из п1.
"""
print("\n\t\tЗадание 10\n")


