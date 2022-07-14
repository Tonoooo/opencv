# Menggambar (Garis, Gambar, Lingkaran & Teks)
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    ## menggambar garis
    # untuk ini kita membutuhkan koordinat awal garis dan akhir garis. kita akan menarik garis diantara 2 titik
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # frame = sumber gambar/video. (0,0) = koordinat awal. (width, height) = posisi akhir. (255, 0, 0) = warnanya biru[ingat urutannya BGR]. 10 = ketebalan garis
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    ## menggambar persegi
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    # (100, 100) = center posisi. (200, 200) = radius. (128, 128, 128) = warna gray. 5 = ketebalan dalam piksel
    ## menggambar lingkaran
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    # (300, 300) = center posisi. 60 = radius. (0, 0, 255) = warna red. -1 = ketebalan[-1 full]
    ## mengambar text
    font = cv2.FONT_HERSHEY_SIMPLEX # menentukan style huruf nya
    img = cv2.putText(img, 'Bismillah', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
    # 'Bismillah' = textnya bebas. (10, height - 10) = center posisi. font = font. 2 = skala font[ukuranya].
    # (0, 0, 0) = wanra hitam. 5 = ketebalan garis. cv2.LINE_AA = tipe garis nya

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()