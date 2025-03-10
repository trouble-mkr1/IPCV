import cv2
import numpy as np 


img = cv2.imread('parzival.webp') 
cv2.imshow("original image", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()


img = cv2.resize(img,(0,0), fx=.5, fy=.5)
cv2.imshow("scaled to half length", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()


(rows, cols) = img.shape[:2] 

 
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1) 
res = cv2.warpAffine(img, M, (cols, rows)) 
cv2.imshow("rotation", res) 
cv2.waitKey(0) 
cv2.destroyAllWindows()


quarter_height, quarter_width = rows / 4, cols / 4
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
img_translation = cv2.warpAffine(img, T, (rows, cols)) 
cv2.imshow('Translation', img_translation) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
