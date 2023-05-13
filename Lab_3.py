
# Veri Setini Filtreleme Operasyonları

import pandas as pd
import os  # os python bir modüldür Operation System (İşletim sistemi) ile ilgili işlemlerde kullanılmaktadır

# excel'den veri okumak için pandas kütüphanesinin read_csv() fonksiyonundan faydalanacağız.
# doc: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

# region Bir dosyanın bulunduğu lokasyonun tam yolunu bize teslim eder
print(os.path.abspath("imdb.csv"))
# endregion
df = pd.read_csv("data/imdb.csv", encoding="utf-8")
# print(df)
# print(df.head(10))  # veri setinin ilk 10 satırını bize teslim eder
# print(df.tail(20))  # veri setinin son 20 satırını bize teslim eder
# # Not: Hem head() hemde tail() fonskiyonlarının default değerleri 5 tir. yani biz bir değer belirtmezsek 5 satırlık bilgi geri döndürürler.
# print(df.shape)
# print(df.info)
# print(df.columns) # sütun isimlerini yazdırır
# print(df["Movie_Title"])  # ilgili sütunda ki bilgileri tesim eder
# print(df["Movie_Title"].head())  # ilgili sütunun ilk 5 satırnı verir.
# print(df[["Movie_Title", "Rating"]].head())  # "Movie_Title", "Rating" sütunlarının ilk 5 satırını getirecek
# print(df[5:20][["Movie_Title", "Rating"]])  # ilgili sütunlardan sadece 5 ile 20'ci satıralarada ki bilgileri getirecek

# Rating'i 8.0'dan büyük olan "Movie_Title", "Rating" sütunlarından verileri getirin.
# print(df[df["Rating"] >= 8.0][["Movie_Title", "Rating"]])

# Yayın tarihi 2014 ile 2018 arasında olan filimlerin isimlerini getiriniz.
# print(df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2018)][["Movie_Title", "YR_Released"]])


# Değerlendime sayısı (Num_Reviews) 100.000'den büyük olan yada imdb puanı 8 ile 9 arasında olan filimleir "Movie_Title", "Rating", "Num_Reviews" sütunlarını getirin.
print(df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title", "Rating", "Num_Reviews"]])


