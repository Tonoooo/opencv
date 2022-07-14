# Pencocokan Template (Deteksi Objek)
import numpy as np
import cv2

# memuat gambar dan jadikan skala abuabu
img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.5, fy=0.5)
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.5, fy=0.5)
h, w = template.shape

# methods pencocokan template
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

## kita akan mencoba semua metod yang berbeda ini dan jika ada metod yang memberi hasil terbaik
# maka kita akan gunakan terus metods tersebut
for method in methods:
    img2 = img.copy()
    # menampilkan matches
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # jadi loop ini akan mencoba loop setiap metods (kita memiliki 6 metods)
    # dan nanti setiap metods akan ada hasil pencocokannya nya

### penjelasan: https://youtu.be/T-0lZWYWE9Y