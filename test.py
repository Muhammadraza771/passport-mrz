print("Script running")
import imquality.brisque as brisque
import PIL.Image
import matplotlib.pyplot as plt
import cv2
from PIL import Image as im
# from paddleocr import PaddleOCR
# ocr = PaddleOCR(use_angle_cls=True,lang="en")



# def crop_mrz_area(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Define the region of interest (MRZ area) coordinates
#     x = 0
#     y = int(image.shape[0] * 0.78)
#     width = image.shape[1]
#     height = int(image.shape[0] * 0.3)

#     # Crop the MRZ area from the image
#     mrz_area = image[y:y+height, x:x+width]
#     temp = im.fromarray(mrz_area)
#     temp.save("ml.jpg")
    # return mrz_area;



# crop_mrz_area('img227.jpg')
# reading image



img = PIL.Image.open("ml.jpg")
print(brisque.score(img))

result = ocr.ocr("ml.jpg")
print(result)

