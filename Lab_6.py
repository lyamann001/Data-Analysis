# Data Frame'leri Birleştirme (Merge-Join)

import pandas
import pandas as pd

customers = {
    'CustomerId': [1, 2, 3],
    'FistName': ["Burak", "Hakan", "İpek"],
    'UserName': ["Beast", "Bear", "Keko"]
}

orders = {
    'OrderId': [1001, 1002, 1003, 1004, 1005],
    'CustomerId': [1, 2, 3, 4, 5],
    "OrderDate": ["2020-07-01", "2022-09-12", "2012-12-12", "2008-02-13", "2012-12-12"]
}

df_customer = pd.DataFrame(customers, columns=["CustomerId", "FistName", "UserName"])
df_orders = pd.DataFrame(orders, columns=['OrderId', 'CustomerId', 'OrderDate'])

print(df_customer)
print(df_orders)

# Merge ederken her iki dataframe'de ortak olan alanların bulunması gerekir. Bizim örneğimizde CustomerId her iki df'te bulunmaktadır.
# DF'leri merge işlemine sokarken sırası önem arz etmektedir. çünkü merge etme şeklimizi bunlar belirlemektedir.
inner_result = pd.merge(df_customer, df_orders, how="inner")  # kesişim datasını verir
outer_result = pd.merge(df_customer, df_orders, how="outer")  # full datayı veriri.
left_result = pd.merge(df_customer, df_orders, how="left")  # kesişim ve sol df tamamını verir
right_result = pd.merge(df_customer, df_orders, how="right")  # kesişim ve sağ df tamamını verir

print(inner_result)
print(outer_result)
print(left_result)
print(right_result)
