import cv2

pic = cv2.imread('Ilhami_Pradini.jpg', 1)
# size_x, size_y = load.shape[1], load.shape[0]
new_pic = cv2.resize(pic, (0, 0), fx = 0.5, fy=0.5)
cv2.imshow('Foto Asli', pic)
cv2.imshow('Foto Baru', new_pic)

cv2.waitKey(0)
cv2.destroyAllWindows()