import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Excel dosyasını oku
file_path = "./data.xlsx"  # Veri dosyanızın yolunu buraya ekleyin
df = pd.read_excel(file_path)

# Veriyi ön işleme
def preprocessing(data):
    # İhtiyaca göre özellikleri dönüştür veya tamamla
    # Örneğin, eksik verileri doldur, kategorik verileri kodla, özellikleri dönüştür vb.

    return data

# Veriyi ön işleme fonksiyonunu uygula
df = preprocessing(df)

# Veriyi eğitim ve test setlerine ayır
x = df.drop('Fiyat', axis=1)
y = df['Fiyat']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Modeli tanımla ve eğit
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Modeli kaydet
with open("train_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

# Modelin performansını değerlendir
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")
