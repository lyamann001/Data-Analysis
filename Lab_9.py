
import pandas as pd
import numpy as np

# df = pd.read_csv("data/automobileData.csv", header=None)
# Not: read_csv() fonsiyonunun yukarıdaki kullanımında veri setinde ki hiç bir sütun başlığı okunmayacaktır. Böylelikle aşağıdaki gibi sütunlara istediğimiz isimleri verebileceğiz.
# headers = ["..", "..."] sütun isimlerimizi verdikten sonra
# df.columns = headers, böylelikle yukarıda oluşturduğumuz sütun isimleri listesini dataframe uygulamış olduk.

df = pd.read_csv("data/auto.csv")
headers = ["symboling", "normalized-losses", "make", "fuel-type","aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers
print(df.head(10))


#  Veri setimizde bazı hücrelerde "?" bulunmaktadır. Bu sembol yerine numpy kütüphanesinde bulunan "nan" değeri basalım.
df.replace("?", np.nan, inplace=True)

#  "?" işareti yerine nan bastık. Şimdi ne kadar "nan" değerimiz var onları sayalım.
missing_data = df.isnull()  # isnull() fonksiyonu ile nan olan değerlerin yerine true olmayan değerelere false basılacak
print(missing_data)

#  Missing Value'ları Sayılması
#  Bir for döngüsü kurarak yukarı true ve false değerleri içeren "missing_data" isimli df içerisinde sütun sütun dolaşabiliriz. Dolaşırken "value_count()" fonskiyonundan faydalanarak bu sütunlarda ki değerleri sayabiliriz
for column in missing_data.columns.values.tolist():
    print(f"Column Name: {column}")
    print("======================")
    print(missing_data[column].value_counts())
    print("\n")

#  Yukarıda ki missing value özetine dayanarak ne kadar eksik bilgi olduğunu saptadık. Eksik değerlerin saptanması çok kilit bir role sahiptir. Artık bu eksik bilgliler üzererinde bakım çalışması yapabiliriz.

#  Eksik Değerler İle Nasıl Başa Çıkılır?
#  1. Eksik değerleri silebiliriz. Lakin bu işlem sonucunda veri setimizde satır kaybı olacaktır. Makine öğrenimine geçtiğimizde veri setinin ne kadar büyük ve homojen yapıda olursa o kadar başarılı sonuçlar aldığımızı göreceksiniz. Bu bağlamda veri setinin küçülmesini istemeyiz. Lakin kayıp göze alınacak boyutta ise eksik değer içeren satır silinebilinir. Bir satırda çok fazla missing value var ise silinir.
#  2. Verileri değiştirme.
#       2.1. Ortalama değer ile değiştirme
#       2.2. Frekans değeri ile değiştirme

#  Ortalma Değer ile Eksik Değerleri değiştirme
#  Bu yöntemde ismindende anlayacağınız gibi eksik değeri içeren sütundaki tüm değerlerin ortalaması alınır. buradaki dikkat edilmesi gereken notka yukarıda eksik değerini np.nan ile doldurduk. Yani birazdan ortlama alırken exception yemeyeceğiz.

avg_normalized_losses = df["normalized-losses"].astype("float").mean()
print(f"Average of normalized-losses: {avg_normalized_losses}")

#  Ortalamayı hesapladık. Artık ilgii sütunda "nan" gördüğümüz yere bu ortalamayı basabiliriz.
df["normalized-losses"].replace(np.nan, avg_normalized_losses, inplace=True)
print(df.head())

# bore sütunundaki ortalama değerleri hesapladık ve ilgili sütunda "nan" gördüğümüz yere ortalama değeri yazdırdık.
avg_bore = df["bore"].astype("float").mean()
print(f"Average of bore: {avg_bore}")

df["bore"].replace(np.nan, avg_bore, inplace=True)
print(df.head())

# Eksik değerleri frekans değer ile değiştirme.
# Frekans değerden kastımız bir sütunda en çok geçen değerdir. Pandas ve python veri bilimi için fantastik işlevler içerir.ç BU frekans değeri hesaplamak için gene farklı farklı fonksiyonlar kullanabiliriz.

print(df["num-of-doors"].value_counts().idxmax())  # ilgili sütunda value_counts() fonskiyonu ile farklı değerleir saydık. "idxmax" ile bu sütunda en çok geçen ifadeyi bulduk. artık bu sütunda nan gördüğümüz yere four ifadesini basabiliriz.

# Veri Standardizasyon
# Değişik ülkelerden yada platformlardan gelen verilerin tek bir standart altında toplanması için yapılan bir işlemdir.

df["city-L/100km"] = 235/df["city-mpg"]
df["highway-L/100km"] = 235/df["highway-mpg"]

# Veri Normalizasyonu
# Belirli bir sutundaki değerlerin benzer bir aralığa dönüştürme işlemine normalizasyon diyoruz. Veri setimizde bulunan lenght, width gibi değerleri 0 ile 1 arasında değerlere dönüştürerek onların normalizasyonunu sağlıyoruz. Böylelikle makine öğrenimi algoritmalarında kulanılanılan matematiksel işlemler daha doğru bir biçimde çalışmaktadır.

df["length"] = df["length"] / df["length"].max()
df["width"] = df["width"] / df["width"].max()
df["height"] = df["height"] / df["height"].max()

print(df[["length", "width", "height"]].head())

# Dummy Variables
# Veri setimizde ki sözel yani categorical yani string diyebileceğimiz veri tiplerini makine öğrenmesi algoritmalarında kullanabilmek için sayısal ifadelere dönüştüreceğiz.

dummy_variable_1 = pd.get_dummies(df["fuel-type"])
print(dummy_variable_1.head())


# Bakımını yaptığımız veri setini kayıt edelim
df.to_csv("clean_df.csv")