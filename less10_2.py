"""Задача 44: В ячейке ниже представлен код
генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?"""

import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

lst = ['robot'] * 10  # В этой строке создается список 10 строк "робот"
lst += ['human'] * 10  # Добавляем список из 10 строк "человек"
random.shuffle(lst)  # Перемешиваем списки с помощью функции shuffle и модуля random
data = pd.DataFrame({'whoAmI': lst})  # Создаем список из перемешаных строк

encoder = OneHotEncoder(sparse_output=False)  # Создаем новый объект
encoder.fit_transform(data[['whoAmI']])  # Создадим столбец
data_head = encoder.fit_transform(data[['whoAmI']])  # Присвоим новые данные
data_head_df = pd.DataFrame(data_head, columns=encoder.categories_[0])  # Создадим новые строки для таблицы
print(data_head_df)  # Вывод данных
