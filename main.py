# Önce pandas ve diğer gerekli kütüphaneleri içe aktaralım, ardından veri setini yükleyip incelemeye başlayalım.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükle
df = pd.read_excel('data.xlsx')

# Özet istatistikler
summary_stats = df.describe()

# Fiyat dağılımı
plt.figure(figsize=(10, 6))
sns.histplot(df['Fiyat'], bins=20, kde=True)
plt.title('Fiyat Dağılımı')
plt.xlabel('Fiyat')
plt.show()

# Korelasyon matrisi
correlation_matrix = df.corr()

# Kategorik değişkenlerin dağılımı
plt.figure(figsize=(12, 6))
sns.countplot(x='İşletim Sistemi', data=df)
plt.title('İşletim Sistemi Dağılımı')
plt.xlabel('İşletim Sistemi')
plt.ylabel('Sayı')
plt.show()
