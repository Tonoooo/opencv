import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    ## warna HSV
    # HSV(hue saturation dan ringan/terang).
    # kita akan mengubah bgr menjadi hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # kita menentukan warna yang ingin kita diekstrak dari gambar
    lower_blue = np.array([90, 50, 50]) # biru muda
    upper_blue = np.array([130, 255, 255]) # biru tua

    ## masks
    # mask adalah semacam bagian dari gambar/frame
    # jika ada piksel yang berwarna biru maka akan aman 1 , jika selain biru akan 0
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    ## menggunakan masks
    # kita menempatkan mask nya ke gambar/video aslinya
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # jadi semua piksel yang bukan biru maka akan jadi hitam. tapi jika ada piksel biru dia akan bertahan

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask) # mask nya akan berupa hitam putih karna jika ada piksel biru akan 1 (putih),selain itu 0 (hitam)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()