import numpy as np
import cv2

img = cv2.imread('assets/catur.png')
# ubah ukuran
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
## mengubah gambarnya jadi skala abuabu
# karena algoritma ini bekerja pada skala abuabu dan
#lebih mudah mendeteksi bagi algoritmanya dari pada pake bgr(blue,green,red)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## menjalankan algoritma deteksi sudut nya
# fungsi goodFeaturesToTrack() memiliki argumen: ( sumber_gambarnya, jumlahsudut, minimum kulitas, jarak minimum euclidean) contoh:
#gray = sumber gambarnya, 100 = jumlah sudut TERBAIK yang ingin direturn
#0.01 = kualitas minimum untuk sudutnya (pilih antara 0-1),
#10 = jarak minimum euclidean antara sudut yang direturn(jarak minimum antar dua sudut)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# mengubah sudut sudutnya menjadi integer
corners = np.int0(corners)

## menggambar sudut sudut nya
for corner in corners:
	x, y = corner.ravel() # untuk meratakan. jadi contoh [[1, 2],[2, 1]] akan menjadi [1, 2, 2, 1]
    # menggambar lingkaran di sudut nya
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

## menggambar garis antar sudut
# jadi setiap sudut akan tersambung satu sama lain menggunakan garis
for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0]) # pertama
		corner2 = tuple(corners[j][0]) # kedua
		## warna nya random
		# map=untuk memetakan semua nilai dari array ke fungsi (disini kita pake fungsi lambda)
		#dan akan mengambalikan array baru yang memiliki semua nilai tersebut
		# lambda = adalah fungsi. dan x disini adalah si np.random nya.
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		# gambar garisnya
		cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()