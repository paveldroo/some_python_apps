import cv2
import glob

filesnames = glob.glob('*.jpg')

for file in filesnames:
    img = cv2.imread(file, 1)
    resized_image = cv2.resize(img, (100, 100))
    cv2.imwrite('resized_{}'.format(file), resized_image)
    cv2.imshow(file, resized_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()