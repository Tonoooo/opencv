# Deteksi Wajah dan Mata
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
## haar cascade
# adalah pengklasifikasian sudah terlatih. fitur untuk mengklasifikasi sudah disediakan oleh opencv
#jadi kita akan menggunakannya.
# memuat wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# memuat mata
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

## menggunakan haar cascade
while True:
    ret, frame = cap.read()
    ## kita menjadikan abuabu dan kemudian akan meneruskan ke cascade dan cascade akan mengembalikan semua lokasi
    #kepada kita
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ## fungsi mendeteksi multi skala dari cascade. jadi ini mendeteksi wajah kita
    #ini akan memberi kita lokasi semua wajah dalam hal posisi.
    # penjelasan parameter: gray = sumber, 1.3 = scaleFactor(Parameter yang menentukan seberapa besar ukuran gambar
    # diperkecil pada setiap skala gambar.), 5 = minNeighbors
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    ## persegi yang digambar disekitar wajah kita
    for (x, y, w, h) in faces: # x dan y = lebar dan tinggi
        ## menggambar persegi di wajah kita
        # (x,y)=sudut kiri atas, (x+w,y+h)=bwah kanan
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        ## mencari tahu area wajah digambar kita. dan gunakan area itu untuk menemukan mata kita
        roi_gray = gray[y:y+w, x:x+w] # mendapatkan lokasi wajah kita
        roi_color = frame[y:y+h, x:x+w] # refrensi ke bingkai asli. jadi dimodifikasi /mengubah bingkai aslinya
        ## deteksi mata yang ada diwajah kita
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        ## mengambar persegi dimata
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

### Penjelasan: https://youtu.be/mPCZLOVTEc4