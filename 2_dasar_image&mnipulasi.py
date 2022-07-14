"""
Sebenarnya gambar direpresentasikan sebagai numpy array.
Ketika kita memuat gambat sebenarnya yang dilakukan adalah mengekstrak piksel dari gambar
dan memuatnya ke numpy array.
"""
import cv2
import random

img = cv2.imread('assets/indah.jpg', -1)

##mengakses nilai piksel
#print(img) # menunjukkan semua pixel . dan ini dalah array numpy.dan disitu terdapat (baris, kolom, channel)
#print(type(img)) # tipe nya numpy array
#print(img[257][45:400]) # meilhat baris pertama ([257]), dan melihat piksel antara 45 sampai 400

"""
##mengubah warna piksel
# meng loop 100 baris pertama dalam gambar kita dengan warna pikse random
for i in range(100): #untuk 100 baris pertama
    for j in range(img.shape[1]): # shape[1] = idex ke-1 di shape adalah kolom, jadi kita ambil kolomnya
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] # ingat BGR = blue green red
# shape = digunakan untuk memberi tahu kita jumlah baris,kolom,dan chanel => (baris, kolom, channel)
"""

## menyalin & menempelkan bagian gambar
#menyalin bagiannya
tag = img[500:700,600:900] # kita mengambil irisin dari arraynya. Baris=500 sampai 700 , kolom=600 sampai 900
#menempelkannya ke bagian lain
img[100:300, 650:950] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()