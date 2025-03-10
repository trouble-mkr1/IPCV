import cv2

img = cv2.imread('goblin_slayer.png')
img = cv2.resize(img,(0,0), fx=.4, fy=.4)
(x,y)=img.shape[:2]
m=int(x/2)
n=int(y/2)
for i in range(x):
    for j in range(y):
        if j==n or i==m:
            img(i,j)=(0,0,0)
cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img)