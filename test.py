import pandas as pd

try:
    data = pd.read_csv(r"C:\Users\johon\Desktop\python\jahongir.csv")

    #print(data.head())

    #print("\nStatistik ma'lumotlar:")
    #print(data.describe())
    #print(data.shape())

     
    nomer = data.select_dtypes(include=['number'])
    katta = nomer[nomer > 1000]
    print(katta)

except FileNotFoundError:
    print("Xatolik: Ko'rsatilgan yo'ldagi CSV fayli topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
