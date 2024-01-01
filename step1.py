
# xlsx dosyasının tüm verilerini çektik. yazdırdık

import pandas as pd

# Excel dosyasını oku
file_path = "./data.xlsx"  # Veri dosyanızın yolunu buraya ekleyin
df = pd.read_excel(file_path)

# Veriyi göster
print(df)
