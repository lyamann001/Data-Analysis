
# Seçme (Select) Operasyonları

import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3, 3),
                  index=["A", "B", "C"],
                  columns=["column1", "column2", "column3"])

print(type(df))
print(df.describe())
print(df.shape)
print(df)
print(df["column1"])

# pandas kütüphanesin sahip olduğu iki önemli yetenek "loc", "iloc"
# Bu arkadaşlar veri setimiz içerisinde nokta atışı hızlı bir şekilde veri çekmemize olanak tanıyacaklar.
# Örnrğin:
# loc["row", "column"] => loc["row"] => loc[":","column"]
# result = df.loc['A']
# result = df.loc[:, ["column1", "column2"]]
# result = df.loc[:, "column2"]
# result = df.loc["B", "column2"]
# result = df.loc[["A", "B"], "column3"]
# result = df.iloc[2]
df["column4"] = df["column1"] + df["column2"]
df.drop("column4", inplace=True, axis=1)
print(df)
