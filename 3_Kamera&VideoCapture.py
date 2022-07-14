import numpy as np
import cv2

## memuat web cam
cap = cv2.VideoCapture(0) # 0 = nomor webcam/perangkat video yang akan digunakan.
#disini kita menggunakan kamera pertama dan kita hanya memiliki 1 webcam saja

## menggunakan webcam
# kita akan gunakan while loop. while loop ini akan menampilkan tersu sampi kita menekan tombol
# di keyboard untuk keluar
while True: #loop tidak terbatas
    ##kita akan mendapatkan bingkai/frame nya deri kamera
    ret, frame = cap.read() # frame = gambarnya(itu akan menjadi array yang mewakili gambar),
    # ret = ini akan memberitahu kita apakah capture berfungsi dengan baik
    ##kita dapatkan tinggi dan lebar videony
    width = int(cap.get(3)) #mendapatkan lebar bingkai, 3 = hanyalah semacam pengidentifikasian untuk properti lebarnya
    height = int(cap.get(4)) # tinggi bingkai
    ### mirroring video beberapa kali
    # ingat di cv2 image direpresentasikan dengan array numpy dan array ini mewakili pixel
    ## kita akan membuat sebuat tempat/kanvas dengan array
    # np.uint8 = ini sebuahtipe artinya bilangan bulat 8 bit
    image = np.zeros(frame.shape, np.uint8) # ini akan mengisi seluruh array dishape kita dengan 0(0=hitam),
    ##menyalin cam nya sebanyak 4 kali
    # kita akan perkecil bingkai
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5) # bingkai diperkecil jadi setengah asli nya
    ## kita akan memasukkan 4 image nya ke dalam kanvas
    # ditempel di sudut kiri atas
    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # rotasi 180 derajat
    # kiri bawah
    image[height//2:, :width//2] = smaller_frame
    # kanan atas
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    # kanan bawah
    image[height//2:, width//2:] = smaller_frame

    ##Menampilkan bingkainya
    cv2.imshow('frame', image)
    ## untuk menutup jedelanya
    if cv2.waitKey(1) == ord('q'):
        break
        # ini akan menunggu hingga 1 milidetik dan jika sampai 1 milidetik maka akan lanjutkan, tapi jika kita
        #tekan tombol dalam 1 milidetik akan mengembalikan nilai ordinal terkait dengan kunci nya

cap.release()
cv2.destroyAllWindows()