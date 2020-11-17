import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Lenna.png")
cv2.imshow("image",img)
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()