import easyocr
import cv2



reader = easyocr.Reader(["en","sv"])

img_path = "img0.jpg"
img = cv2.imread(img_path)
#result = reader.readtext(img, detail=0)

print(result)



print("process return 0")