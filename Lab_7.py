import pandas as pd

df = pd.read_csv("data/nba.csv")

# En yüksek maaşı alan oyuncu kimdir?
# result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]


# Yaşı 20 ile 25 arasında olan oyuncuların isim ve oynadıkları takımı yaşlarına göre çoktan aza sıralayarak getiriniz
# result = df[(df["Age"] >= 20) & (df["Age"] <= 25)][["Name", "Team", "Age"]].sort_values("Age", ascending=False)


# "John Holland" isimli oyuncunun oynadığı takımı hangisidir?
# result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# Takımlara göre oyuncuların ortalama maaş bilgisi nedir?
# result = df.groupby("Team")["Salary"].mean()

# Kaç farklı takım mevcut?
# result = df["Team"].nunique()
# result = len(df.groupby("Team"))
# result = df.groupby("Team").value_counts() # bu sorgu sonucunda takımları gruplayarak tüm bilgisini bize temsil edder.

# Her takımda kaç oyuncu oynamaktadır?
# result = df["Team"].value_counts()

# ismi içinde "and" geçen oyuncuları listeleyin
df.dropna(inplace=True)  # aşağıda ki satırda ki kod çalıştırışdığında exception (ValueError: Cannot mask with non-boolean array containing NA / NaN values) yedik. Bu hatada gördüğünüz gibi NaN değerlerden dolayı hata alıyoruz. Bu sebepten NaN değerleri drop ettik.


# result = df[df["Name"].str.contains("and")]

# İsmi içerisinde "and" ifadesi geçen oyuncuları bulalım. bu işlem için bir fonksiyon yazalım.

def str_find(name: str):
    if "and" in name.lower():
        return True
    else:
        return False


# Yukarıda yazdığımız fonksiyon contains() fonksiyonu görevini yerine getirecek. Peki yazdığımız bu custom fonksiyonnu nasıl bir dataframe'in sütununa uygulayacağız?

result = df[df["Name"].apply(str_find)]

print(result)

# str_find() fonskiyonu sadece ismi içerisinde "and" geçen oyuncuları listelemektedir. "and" değerinide dinamikleştirerek bu örneği tekrardan yapalım.
# 1. adım: df["Name"] sutununda ki değerleri alacağız.
# 2. adım: bir loop'a sokacağız. loop'un bir adınımda bir ismi "str_find_v1" fonksiyonuna göndereceğiz.

