


import pandas as pd
import numpy as np

number = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd']
scaler = 5
dictionary = {'a': 10, 'b': 20, 'c': 30}
np_arrays = np.array([20, 30, 40, 50])

# pd_series = pd.Series(number)
# pd_series = pd.Series(letters)
# pd_series = pd.Series(scaler)
# pd_series = pd.Series(dictionary)
pd_series = pd.Series(np_arrays)
print(pd_series)
print(pd_series[:2])  # liste yapısında öğrendiğimiz index'leme ve slicing mantığı pandas Series'ta geçerlidir.
print(pd_series.ndim)
print(pd_series.dtype)
print(pd_series.shape)
print(pd_series.describe())
print(pd_series.head(2))
print(pd_series.sum())
print(pd_series >= 30)
print(pd_series % 2 == 0)

opel2018 = pd.Series([20, 30, 40], ["astra", "corsa", "mokka"])
opel2019 = pd.Series([50, 10, 90], ["astra", "corsa", "mokka"])

total = opel2018 + opel2019  # karşılık gelen değerleri topladık
# index bilgileri bu sefer araç isimleri olarak dizay edildi
print(total)
print(total["astra"])  # astra'da tutulan değerler
#print(total["qwe"])  # KeyError: 'qwe'

# s1 = pd.Series([3, 2, 4, 5])
# s2 = pd.Series([1, 9, 7, 8])
#
# data = dict(apple=s1, orange=s2)
#
# df = pd.DataFrame(data)  # pandas kütüphanesinin birincil veri tipi data frame'dir. genellikle "df" kısaltması ile ifade edilir. Excel gibi satır ve sütunlardan oluşan bir yapısı mevcuttur. Veri biliminde yoğun olarak kullanılmaktadır.

# dataInfo = [["Cihat", 10], ["İrfan", 39], ["İbo", 50], ["Okan", 1]]

# df = pd.DataFrame(dataInfo)  # dataInfo isimli listeyi data frame tipine dönüştürdük

# grades = {
#     "Name": ["Cihat", "İrfan", "İbrahim", "Okan"],
#     "Garde": [50, 60, 70, 80]
# }

# df = pd.DataFrame(grades)

dict_list = [
    {"Name": "Cihat", "Grade": 50},
    {"Name": "İrfan", "Grade": 40},
    {"Name": "İbo", "Grade": 30},
    {"Name": "Okan", "Grade": 20},
]

df = pd.DataFrame(dict_list)

print(df)
