# Work with missing data

import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index=['a', 'b', 'c', 'e', 'f'], columns=['Column1', 'Column2', 'Column3'])

# df = df.reindex(['z', 'x', 'y', 'w', 'v'])
# Yukarıadaki satır çalıştırıldığın data frame "NaN" değerler ile doldu yani boş.

newColumn = [np.nan, 30, np.nan, 51, np.nan]
df["Column4"] = newColumn

# df.drop("Column1", axis=1, inplace=True)  # Column1 isimli sütunu siler
# df.drop("a", axis=0, inplace=True)  # Bütun sütunlardan a indexsinde bulunan değerleri sile
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

# result = df.isnull()  # Eğer veri setinde "NaN" değerler varsa True yoksa False döner

# result = df.isnull().sum()  # Data frame içerisinde kaç tane null değer varsa sütun bazında bize toplamını döner

# result = df.notnull().sum()["Column1"]  # sütun 1'de NaN olmayan değerlerin toplamını bize verdi

# result = df.fillna(value=1)  # Sütunda "NaN" gördüğü yere 1 değeri bastırdık.

result = df.dropna()  # NaN değerleri drop ettik

print(result)
