#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:08:30 2023

@author: emredikici
"""

import pandas as pd
import random
from faker import Faker
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


fake = Faker()

# Rastgele sporcu bilgileri oluşturma
data = {
    'Sporcu Adı': [fake.name() for _ in range(50)],
    'Şehir': [fake.city() for _ in range(50)],
    'Cinsiyet': [random.choice(['Erkek', 'Kadın']) for _ in range(50)],
    'Takım': [fake.company() for _ in range(50)],
    'Madalya Çeşidi': [random.choice(['Altın', 'Gümüş', 'Bronz']) for _ in range(50)],
    'Tarih': [fake.date_of_birth(minimum_age=18, maximum_age=40) for _ in range(50)],
    'Kazandığı Maç Sayısı': [random.randint(1, 100) for _ in range(50)]
}

# Veri setini DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Veriyi CSV dosyasına kaydetme
df.to_csv('sporcu_veri_seti.csv', index=False)





# *********** MEAN-ROUND-VAR-STD ***********
"""
# ortalama = np.mean(veri) bu şekilde de bulunabilir.
mean_value = df["Kazandığı Maç Sayısı"].mean()
print(mean_value)


round_value = round(df["Kazandığı Maç Sayısı"])
print(round_value)


# Varyans Hesaplama
varyans = np.var(df)
print("Varyans:", varyans)


# Standart Sapma Hesaplama
standart_sapma = np.std(df)
print("Standart Sapma:", standart_sapma)
"""




# *********** İSNULL ***********
#isnull() fonksiyonu, bir veri çerçevesi veya dizi içindeki her bir elemanın eksik (NaN) olup olmadığını kontrol etmek için kullanılır. Bu fonksiyon, True veya False değerlerinden oluşan bir boolean dizi döndürür.
"""
eksik_mi = df.isnull()
print(eksik_mi)
"""



# *********** FİLLNA ***********
# örnek bir veri seti oluşturdum ve bu veri seti boş kalan değerleri 0 ile doldurdu
"""
veri = pd.Series([1, 2, np.nan, 4, np.nan, 6])
veri_doldurulmus = veri.fillna(0)  # NaN değerleri 0 ile doldur
print(veri_doldurulmus)
"""
# ortalama ile veri doldurma
"""
veri = pd.Series([1, 2, np.nan, 4, np.nan, 6])
ortalama = veri.mean()
veri_doldurulmus = veri.fillna(ortalama)  # NaN değerleri ortalama ile doldur
print(veri_doldurulmus)
"""




# *********** HEAD - TAİL ***********

"""
# head(5) ilk 5 elemanı tail(5) son 5 elemanı gösterir
print(df.head(5),df.tail(5))
"""







# *********** İNFO ***********
#print(df.info())
"""
#   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   Sporcu Adı            50 non-null     object
 1   Şehir                 50 non-null     object
 2   Cinsiyet              50 non-null     object
 3   Takım                 50 non-null     object
 4   Madalya Çeşidi        50 non-null     object
 5   Tarih                 50 non-null     object
 6   Kazandığı Maç Sayısı  50 non-null     int64 
dtypes: int64(1), object(6)
"""




# *********** SHAPE ***********
# Veri çerçevesinin satır ve sütun sayısını alma.
print(df.shape)





# *********** DESCRİBE ***********
#print(df.describe())
"""
       Kazandığı Maç Sayısı
count             50.000000
mean              49.180000
std               31.427071
min                1.000000
25%               18.000000
50%               55.000000
75%               76.500000
max              100.000000
"""







# *********** COLUMNS ***********
#print(df.columns)
"""
Index(['Sporcu Adı', 'Şehir', 'Cinsiyet', 'Takım', 'Madalya Çeşidi', 'Tarih',
       'Kazandığı Maç Sayısı'],
      dtype='object')
"""





# *********** RENAME ***********
"""
# Şehir isimli satırı Ülke ismi ile değiştirir.
df.rename(columns={'Şehir' : 'Ülke'},inplace = True)
"""





# *********** DROP ***********
"""
# ülke isimli satırı siler
df = df.drop(["Ülke"],axis=1)
"""







# *********** UNİQUE ***********
"""
# farklı şehir sayılarını bulur
sehir = pd.unique(df["Şehir"])
print("Unique olan şehir : {}".format(len(sehir)))
"""





# *********** SORT VALUES ***********
# aldığı madalya çeşidine göre sporcular sıralandı
"""
madalya_cesidine_gore_sıralama = df.sort_values(by='Madalya Çeşidi')
print(madalya_cesidine_gore_sıralama)
"""





# *********** GROUP BY ***********
# groupby ile cinsiyetler gruplara ayrılır. ve her bir cinsiyetin kazandıklareı maç sayıları toplanır.
cinsiyet_grubu = df.groupby('Cinsiyet')
mac_sayisi = cinsiyet_grubu['Kazandığı Maç Sayısı'].sum()
print(mac_sayisi)
"""
Cinsiyet
Erkek    1317
Kadın     845
Name: Kazandığı Maç Sayısı, dtype: int64
"""






"""
# filtre belirleyerek işlem yapma
# Kazandığı Maç Sayısı > 50 olan değerler için filtre oluşturur
filtre = df["Kazandığı Maç Sayısı"] > 50

gecici_veri = df[filtre]

print(gecici_veri)
"""


















#         ******************** MATPLOTLİB KÜTÜPHNAESİ ********************



# girilen değerlere göre çizgi grafiği oluşturma
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints)
plt.show()
"""




# *********** COLOR VE MARKER KULLLANIMI ***********

# color ve marker komutları ile renk belirlendi değerler marker ile işaretlendi
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints,color = "red", marker = "o")
plt.show()
"""





# hem rengi hem de çizgilerin çeşidini belirler
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints, 'o--')# 'o-r'   'o:r'  'o--'  'o-.'
plt.show()
"""





# *********** MS KULLANIMI ***********
# belirlenen marker simgesini büyültür
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints,color = "red", marker = "o",ms=49)
plt.show()
"""




# *********** MEEC KULLANIMI ***********
#markerların çevresinin rengini belirler
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints,color = "red", marker = "o",mec="black")
plt.show()
"""






# *********** MFC KULLANIMI ***********
# markerların içinin rengini belirler
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints,color = "red", marker = "o",ms=20,mfc = "green")
plt.show()
"""






# *********** LİNESTYLE KULLANIMI ***********
# grafikteki çizgilerin çeşitlerini değiştirir
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints,linestyle = 'dotted')
plt.show()
"""
#linstyle çeşitleri
'solid' 	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'



# yukarıdaki örneği kısaltarak ls diye yazabiliriz.
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints,ls = '--')
plt.show()
"""









# *********** LİNEWİDTH KULLANIMI ***********
# grafikteki çizgi kalınlığını belirler
"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints,linewidth = '20.5')
plt.show()
"""







# aynı grafikte iki çizgi gösterimi
"""
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
"""





"""
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
"""











# *********** LABEL VE TİTLE ***********
# Label ve title kullanımı
"""
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
"""







# *********** LOC ***********
# loc ile title a locaiton atayabiliriz
"""
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data", loc="left")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
"""











# *********** GRİD ***********
# ızgara ekler
# plt.grid(axis = "x") x ekseninde grid çizer
# plt.grid(axis = "y") y ekseninde grid çizer

"""
xpoints = np.array([0,1,2,3,4,5,6,7,8])
ypoints = np.array([0,1,4,9,16,25,36,49,64])

plt.plot(xpoints, ypoints)
plt.grid()
plt.show()
"""











# gridleri özelleştirme
"""
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()
"""









# *********** SUBPLOT KULLANIMI  ***********


# subplot (alt grafik): Matplotlib kütüphanesinde birden fazla grafik veya çizim panelini aynı figür üzerinde düzenlemek için kullanılan bir işlemdir. 


#İlk parametre (1): Alt grafiklerin toplam satır sayısını belirtir.
#İkinci parametre (2): Alt grafiklerin toplam sütun sayısını belirtir.
#Üçüncü parametre (1): Şu anda oluşturulan alt grafiklerden hangisinin aktif olduğunu belirtir.
"""
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
"""






# subplot kullanımı ile 6 grafik tek ekranda
"""

plt.figure(figsize=(10, 10)) # başlıklar ile değerler iç içe girmesin diye alanı ayarladım


x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title("SALES")



x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title("SALES1")



x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title("SALES2")



x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.title("SALES3")



x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.title("SALES4")



x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title("SALES5")


plt.suptitle("MY deneme")


plt.show()
"""





"""
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 18, 20]
y2 = [5, 8, 7, 9, 11]

plt.plot(x, y1, label='Çizgi 1')
plt.plot(x, y2, label='Çizgi 2')
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')
plt.title('Birden Fazla Çizgi Grafiği')
plt.legend()
plt.show()
"""









# *********** SCATTER KULLANIMI  ***********

"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
"""




# iki tane scatter ile karşılaştırma işlemleri yapma
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()
"""






# renk kullanarak ayırt etme
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()
"""






# girilen her bir değer için farklı renklerde nokta yapma
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()
"""













# *********** COLORMAP VE COLORBAR ***********



# colormap ve colorbar kullanımı
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='inferno') # plasma,inferno,viridis,magma,cividis gibi örnek renk barları vardır
plt.colorbar()

plt.show()
"""







# boyutlarını kemdi değerlerine göre ayarlama
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()
"""











# alpha değeri ile saydamlık ayarlanır
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.4)

plt.show()
"""


















# *********** BARS KULLANIMI ***********

"""
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
"""






# horizontal grafik (yan yatmış
""")
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()
"""







# color kullanımı
"""
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()
"""




# width ile grafik genişliği ayarlama
"""
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()
"""
















# *********** HİSTOGRAM KULLANIMI ***********

"""
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 
"""






# alpha , title, grid ve label kullanımı
"""
veri = np.random.randn(1000)  # 1000 adet rastgele sayı üretir

plt.hist(veri, bins=30, color='blue', alpha=0.4)
plt.xlabel('Değerler')
plt.ylabel('Frekans')
plt.title('Rastgele Veri Histogramı')

plt.grid()

plt.show()
"""














# *********** PİE CHART KULLANIMI ***********


"""
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
"""




# label kullanımı
"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()
"""








# explode ile grafik dilimleri arasını açma
"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0.1, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
"""










# shadow ile gölge ekleme
"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 
"""








# color kullanımı
"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()
"""








# legend kullanımı, başlık verilmesi  ve konumu ayarlanması

"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(loc="upper left",title = "Four Fruits:") # loc=(1 ,0.5) şeklinde özel olarak da ayarlanabilir
plt.show() 
"""




















#            ******************* SEABORN KÜTÜPHNAESİ ********************
#Seaborn, Python programlama dilinde veri görselleştirmesi yapmak için kullanılan bir veri görselleştirme kütüphanesidir. Seaborn, Matplotlib'e dayalıdır ve veri analizi süreçlerinde veriyi daha çekici ve bilgilendirici şekillerde görselleştirmek için kullanılır.



# *********** HİSTPLOT KULLANIMI ***********
"""
sns.set(style="white")

# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)

# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")
"""






#HUE kullanımı
"""
penguins = sns.load_dataset("penguins")


# Plot Histogram
sns.histplot(data = penguins, x = "body_mass_g", kde = True, hue = "species")
"""









#STAT ve DİSCRETE kullanımı
"""
# Load dataset
tips = sns.load_dataset("tips")

# Plot histogram
sns.histplot(data = tips, x = "size",stat = "probability",  discrete = True)

"""








# *********** SCATTERPLOT KULLANIMI ***********

"""
# Örnek bir veri seti oluşturalım
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [3, 5, 6, 8, 9, 10, 12, 14, 15, 17]
})

# Scatterplot çizimi
sns.scatterplot(x='X', y='Y', data=data)
plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('X ve Y Değerleri Arasındaki İlişki')
plt.show()
"""






#HUE kullanımı
"""
# Kategorik bir veri seti oluşturalım
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [3, 5, 6, 8, 9, 10, 12, 14, 15, 17],
    'Kategori': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

# Scatterplot çizimi ve renklendirme
sns.scatterplot(x='X', y='Y', hue='Kategori', data=data)
plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('X ve Y Değerleri Arasındaki İlişki (Kategoriye Göre Renklendirme)')
plt.show()
"""









"""
# Veri setini oluşturalım
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [3, 5, 6, 8, 9, 10, 12, 14, 15, 17],
    'Büyüklük': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# Scatterplot çizimi ve noktaları büyüklüğe göre ayarlama
sns.scatterplot(x='X', y='Y', size='Büyüklük', data=data)
plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('X ve Y Değerleri Arasındaki İlişki (Nokta Büyüklüğüne Göre Ayarlama)')
plt.show()
"""










# PALETTE kullanımı
"""
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [3, 5, 6, 8, 9, 10, 12, 14, 15, 17],
    'Kategori': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

# Scatterplot çizimi ve renklendirme
sns.scatterplot(x='X', y='Y', hue='Kategori', data=data)
sns.set_palette("husl") # muted,pastel,dark,colorblind gibi türleri var.


plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('X ve Y Değerleri Arasındaki İlişki (Kategoriye Göre Renklendirme)')
plt.show()
"""











# MARKER kullanımı
"""
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [3, 5, 6, 8, 9, 10, 12, 14, 15, 17],
    'Kategori': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

# Scatterplot çizimi ve renklendirme
sns.scatterplot(x='X', y='Y', hue='Kategori', marker='*', data=data)
plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('X ve Y Değerleri Arasındaki İlişki (Kategoriye Göre Renklendirme)')
plt.show()
"""











# ALPHA kullanımı
"""
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [3, 5, 6, 8, 9, 10, 12, 14, 15, 17],
    'Kategori': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

# Scatterplot çizimi ve renklendirme
sns.scatterplot(x='X', y='Y', hue='Kategori', alpha=0.3,data=data)
plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('X ve Y Değerleri Arasındaki İlişki (Kategoriye Göre Renklendirme)')
plt.show()
"""










# *********** LİNEPLOT KULLANIMI ***********







# HUE kullanımı
"""
sns.set(style="darkgrid")

data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [3, 5, 6, 8, 9, 10, 12, 14, 15, 17],
    'Kategori': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

# Scatterplot çizimi ve renklendirme
sns.lineplot(x='X', y='Y', hue='Kategori', alpha=0.3,data=data)
plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('X ve Y Değerleri Arasındaki İlişki (Kategoriye Göre Renklendirme)')
plt.show()
"""













# *********** BARPLOT KULLANIMI ***********




"""
# from seaborn library
df = sns.load_dataset('titanic')

# class v / s fare barplot
sns.barplot(x = 'class', y = 'fare', data = df)

# Show the plot
plt.show()
"""














#HUE kullanımı
"""
# from seaborn library
df = sns.load_dataset('titanic')

# class v / s fare barplot
sns.barplot(x = 'class', y = 'fare', hue = 'sex', data = df)

# Show the plot
plt.show()
"""








# ORDER kullanımı
"""
# from seaborn library
df = sns.load_dataset('titanic')

# class v / s fare barplot in given order
sns.barplot(x = 'class', y = 'fare', data = df,
			order = ["Third", "Second", "First"])

# Show the plot
plt.show()
"""








#COLOR kullanımı
"""
df = sns.load_dataset('titanic')

# class v / s fare barplot with same colour
sns.barplot(x = 'class', y = 'fare', data = df, color = "salmon")

# Show the plot
plt.show()
"""












# SATURATİON kullanımı
"""
# from seaborn library
df = sns.load_dataset('titanic')

sns.barplot(x = 'class', y = 'fare', hue = 'sex', data = df,saturation = 0.4)

# Show the plot
plt.show()
"""











# FACECOLOR , LİNEWİDTH, EDGECOLOR, ERRCOLOR kullanımı
"""
df = sns.load_dataset('titanic')

sns.barplot(x="class", y="fare", data=df,
				linewidth=2.5, facecolor=(1, 1, 1, 0),
				errcolor=".7", edgecolor=".5")
"""









# *********** COUNTPLOT KULLANIMI ***********

"""
df = sns.load_dataset('tips')

# count plot on single categorical variable
sns.countplot(x ='sex', data = df)

# Show the plot
plt.show()
"""








"""
df = sns.load_dataset('tips')

# count plot on two categorical variable
sns.countplot(x ='sex', hue = "smoker", data = df)

# Show the plot
plt.show()
"""




"""
df = sns.load_dataset('titanic')

# class v / s fare barplot
sns.countplot(x ='sex', data = df,color="salmon", facecolor=(0, 0, 0, 0),
				linewidth=5,
				edgecolor=sns.color_palette("BrBG", 2))
# Show the plot
plt.show()

"""












