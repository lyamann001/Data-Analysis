# Gruplama (Groupby) Operasyonları

import pandas as pd
import numpy as np

personller = {
    'Çalişan': ['Burak Yılmaz', 'İrfan Bayrak', "Okan Demirel", 'Cihat Aksoy', 'Ömer Umut', 'İbrahim Akkaş'],
    'Departman': ['Kumarbaz', 'Hacker', 'Simyacı', 'Kumarbaz', 'Düzenbaz', 'Düzenbaz'],
    'Yaş': [33, 23, 32, 23, 34, 33],
    'Semt': ["Sarıyer", "Bostancı", "Bostancı", "Balat", "Balat", "Bostancı"],
    'Maaş': [5200, 5200, 5300, 5400, 5300, 100000]
}

df = pd.DataFrame(personller)
# print(df)

# print(f'Toplam Maaş: {df["Maaş"].sum()}')
# print(df.groupby("Semt").groups)

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)


# hangi semt'ye kaç tane çalışanım var
# result = df.groupby("Semt")["Çalişan"].count()
# print(pd.DataFrame(result, columns=["Region", "Count"]))


# Departmanlara göre grouplayalım, hangi departmana ne kadar maaş veriyorum
# print(df.groupby("Departman")["Maaş"].sum())

# Departmanı "Kumazbaz" olan maksimum maaşa sahip olan çalışanı getirin
print(df.groupby("Departman")["Maaş"].max().loc["Kumarbaz"])

# Departmanlara göre yaş ortalaması
print(df.groupby("Departman")["Yaş"].mean())

# Düzenbaz mesleğine sahip kişilerden en küçük yaşa sahip olan
print(df.groupby("Departman")["Yaş"].min().loc["Düzenbaz"])

print(df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min]))