import pandas as pd

df = pd.read_csv("data/youtube-ing.csv")

# thumbnail_link, comments_disabled, ratings_disabled, description, video_error_or_removed sütunlarını silelim
df.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'description', 'video_error_or_removed'],
        inplace=True, axis=1)

# En çok görüntülenen video hangisi
# result = df[df["views"] == df["views"].max()]["title"].iloc[0]


# En çok görüntülenen ilk 10 video (title, views) sütunları ile birlikte getirin
# result = df.sort_values(by="views", ascending=False).head(10)[["title", "views"]]

# Kategorilerine göre beğeni ortalamalarını sıralı şekilde getiriniz
# result = df.groupby("category_id").mean().sort_values("likes", ascending=False)["likes"]

# Her katagoride kaç video vardır
# result = df["category_id"].value_counts()

# Kategorilerine göre yorum sayılarını yukarıdan aşağıya doğru sıralayınız
# result = df.groupby("category_id").sum().sort_values(by="comment_count", ascending=False)["comment_count"]


# Her video için kullanılan tag sayısını yeni kolonda gösteriniz
# Yol I
# def tag_count(tag):
#     return len(tag.split('|'))
#
#
# df["tag_count"] = df["tags"].apply(tag_count)
# Yol II
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))

# Her bir video listeleyiniz (like ve dislike oranına göre)
# Beğeni oranı olarak yeni bir sütun oluşturun (beğeni oranını hesaplamak için fonksiyon)
# like ve dislike sutunlarını list'ye alalım bu listeleri zip() fonksiyonu ile birleştirelim
# bu sütuna göre çoktan aza sıralayın.
# sonuç kümesinde title, like, dislike, like_avarage sütunları olsun

def likeDislikeOranHesapla(dataSet):
    likeList = list(dataSet["likes"])
    dislikeList = list(dataSet["dislikes"])

    liste = list(zip(likeList, dislikeList))

    oranListesi = []

    for like, dislike in liste:
        if like + dislike == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like + dislike))

    return oranListesi


df["like_avarage"] = likeDislikeOranHesapla(df)

result = df.sort_values(by="like_avarage", ascending=False)[["title", "likes", "dislikes", "like_avarage"]]

print(result)

