"""
open CV adalah libary computer vision open source yang digunakan untuk menganalisa image, video,
image processing, manipulasi pengolahan, mendeteksi objek, pengenalan wajah dan banyak lagi.
"""

import cv2

## memuat gambar
img = cv2.imread('assets/langit.jpg', 1)
# cv2 akan memmuat gambar kita dalam warna biru,hijau,merah. Dan kita memiliki 3 opsi mode:
# -1 => cv2.IMREAD_COLOR = memuat gambar berwarna. dan transpran apapun akan diabaikan. ini default
# 0 => cv2.IMREAD_GRAYSCALE = memuat gambar dalam mode skala abu-abu, hitam putih
# 1 => cv2.IMREAD_UNCHANGED = memuat gambar seperti itu termasuk saluran alfa, jadi transparannya tidak akan diabaikan

## mengubah ukuran gambar
img = cv2.resize(img, (400,400)) # tinggi dan lebat dalam pixel
# cara lain => ((0,0), fx=2,fy=2) => 2 berarti besarnya 2 kali dar ukuran aslinya. 0,0 ini hanya default tidak terlalu penting

## rotate image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
#ROTATE_90_CLOCKWISE = 90 DERAJAT ARAH JARUM JAM
#ROTATE_90_COUNTERCLOCKWISE = 90 DERAJAT BERLWANAN JARUM JAM
#itu angka nya bisa bebas tidak hanya 90 saja

## menyimpan salinan gambar
cv2.imwrite('1kasihnama.jpg', img) # memiliki 2 parameter: 'nama_file_barunya.jpg'  dan sumber/gambar yang maudisalin

## menampilkan gambar
cv2.imshow('image', img) # parameter => ('nama/labelnya dijedelanya', gambarnya)
# untuk menutup jedelanya
cv2.waitKey(0) # menunggu menutup jendela sampai waktu yang ditentukan saat anda untuk menemkan tombol mana saja. 0 = waktunya tak terbatas. jika selain 0 itu waktu, contoh 10 berati waktunya hanya 10 milidetik untuk
#menggu sampai mengetikkan apapun, jika tidak ada ketikan maka aka ditutup menggunakan:
cv2.destroyAllWindows() # menyingkirkan semua jendela