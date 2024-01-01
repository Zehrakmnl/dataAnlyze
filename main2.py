import pandas as pd

# Veri setini yükle
df = pd.read_excel('./data.xlsx')

# Kayıt sayıları
kayit_sayisi = len(df)

# Nitelik sayıları
nitelik_sayisi = len(df.columns)

# Nitelik tipleri
nitelik_tipleri = df.dtypes

# Merkezi eğilim ölçüleri
ortalama = df.mean()
medyan = df.median()
mod = df.mode().iloc[0]  # mod() bazen birden fazla mod döndürebilir, ilk değeri alıyoruz

# Merkezden dağılım ölçüleri
standart_sapma = df.std()
minimum = df.min()
maksimum = df.max()

# 5 sayı özeti
bes_sayi_ozeti = df.describe().transpose()[['min', '25%', '50%', '75%', 'max']]

# Sonuçları görüntüle
print("Kayıt Sayısı:", kayit_sayisi)
print("\nNitelik Sayısı:", nitelik_sayisi)
print("\nNitelik Tipleri:\n", nitelik_tipleri)
print("\nOrtalama Değerler:\n", ortalama)
print("\nMedyan Değerler:\n", medyan)
print("\nMod Değerler:\n", mod)
print("\nStandart Sapma:\n", standart_sapma)
print("\nMinimum Değerler:\n", minimum)
print("\nMaksimum Değerler:\n", maksimum)
print("\n5 Sayı Özeti:\n", bes_sayi_ozeti)
