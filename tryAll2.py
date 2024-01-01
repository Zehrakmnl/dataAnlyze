import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pickle

# Excel dosyasını oku
file_path = "./data.xlsx"  # Veri dosyanızın yolunu buraya ekleyin
df = pd.read_excel(file_path)

# Veriyi ön işleme
def preprocessing(data):
    # Kategorik sütunları sayısal değerlere dönüştür
    label_encoder = LabelEncoder()
    categorical_columns = data.select_dtypes(include=['object']).columns
    data[categorical_columns] = data[categorical_columns].apply(label_encoder.fit_transform)

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

# Örnek bir çıktı
print("Veri setinin ilk 5 satırı:\n", df.head())

# Eğitim verisi üzerindeki performans sonuçları
print("Eğitim verisi performansı:", accuracy)

# Test verisi üzerindeki performans sonuçları
# print("Test verisi performansı:", performans_test)

# Bu çıktıları bir dosyaya kaydetmek için örnek
with open("output.txt", "w") as file:
    file.write("Veri setinin ilk 5 satırı:\n" + str(df.head()) + "\n")
    file.write("Eğitim verisi performansı:" + str(accuracy) + "\n")
    # file.write("Test verisi performansı:" + str(performans_test) + "\n")

# Şu adımları gerçekleştirdik:

# Veri Okuma: Pandas kütüphanesini kullanarak Excel dosyanı pd.read_excel ile okudun ve bir DataFrame'e dönüştürdük.

# Veri Ön İşleme: preprocessing fonksiyonunu tanımlayarak, veri setindeki kategorik sütunları sayısal değerlere dönüştürdük. 
# Bu adım, makine öğrenimi modellerinin çalışabilmesi için önemlidir.

# Veriyi Eğitim ve Test Setlerine Ayırma: train_test_split fonksiyonunu kullanarak veriyi eğitim ve test setlerine böldük. 
# Bu, modelin eğitim sırasında kullanılacak veriyi ve daha sonra performansını değerlendirmek için kullanılacak test verisini belirler.

# Modeli Tanımlama ve Eğitme: RandomForestClassifier'ı kullanarak bir model tanımladın ve eğitim verisi üzerinde bu modeli eğittik.

# Modeli Kaydetme: Eğitilmiş modeli pickle ile train_model.pkl adlı bir dosyaya kaydettik. Bu, daha sonra bu modeli tekrar kullanmak 
# istediğinde kullanılabilir.

# Model Performansını Değerlendirme: Eğitilen modeli test seti üzerinde değerlendirdin ve accuracy_score ile modelin doğruluğunu ölçtük.
# Bu, modelin ne kadar iyi performans gösterdiğini gösterir.