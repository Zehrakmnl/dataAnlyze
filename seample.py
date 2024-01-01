def preprocessing(data):
    # Özellik ölçeklendirme işlemi (örneğin, standartlaştırma veya 
    #normalleştirme)
    data ['Özellik_1'] ... = normalizasyon(data ['Özellik_1']),
    # Eksik verilerin doldurulması
    data=fill_missing_data(data)
    # Kategorik verilerin kodlanması (örneğin, one-hot encoding)
    data= one_hot_encoding(data['Kategorik_Ozellikler'])
    return data

def classification(data):
    data= read('data.xlsx') # Eğitim verisini yükle
    data = preprocessing(data) # Ön işleme adımlarını uygula
    x= data.drop('Fiyat', axis=1) # Bağımsız değişkenler
    y= data['Fiyat'] # Bağımlı değişken
    x_train, x_test, y_train, y_test = train_test_split(x, y, 
    test_size=0.2, random_state=42)
    model= #Kullanacağın modeli tanımla
    model = model.fit (x_train, y_train)
    model.save(“train_model”)
    performans = model.predict( x_test, y_test)
    # Test verisiyle modelin performansını değerlendir
    
def test(data):
test_data = oku('data.xlsx') # Test verisini yükle
test_data = preprocessing(test_data) # Eğitimde yapılan 
# ön işlemleri test verisine uygula
test_x = test_data.drop('Fiyat', axis=1) # Bağımsız değişkenler
test_y = test_data ['Fiyat'] # Bağımlı değişken
model=load(“train_model)
performans = model.predict( test_x, test_y)