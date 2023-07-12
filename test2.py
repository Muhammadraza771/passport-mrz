from paddleocr import PaddleOCR

from brisque import BRISQUE
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy
import cv2
from skimage import io
from PIL import Image as im, ImageOps

ocr = PaddleOCR(use_angle_cls=True,lang="en")



def crop_mrz_area(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Define the region of interest (MRZ area) coordinates
    x = 0
    y = int(image.shape[0] * 0.78)
    width = image.shape[1]
    height = int(image.shape[0] * 0.3)

    # Crop the MRZ area from the image
    mrz_area = image[y:y+height, x:x+width]
    temp = im.fromarray(mrz_area)
    temp.save("passport/ml.jpg");
    # return mrz_area;

path = 'poor7.jpg'
img = io.imread(path);
obj = BRISQUE(url=False)

score = obj.score(img)

def getMrz(imgPath):
  print("img :: ",imgPath)
  crop_mrz_area(imgPath);
  factor=0;
  if score>40:
    factor = 1.25
  elif score <25:
    factor = 1.4
    # factor = 1.6
  else:
    factor = 1.1

  print("factor:: ",factor)  
  im = Image.open("passport/ml.jpg")
  enhancer2 = ImageEnhance.Brightness(im)
#   factor = 1.25 #brightens the image
  im_output = enhancer2.enhance(factor)
  im_output.save('passport/ml.jpg')

#   factor = 3.2 #increase contrast

  im = Image.open("passport/ml.jpg")
  enhancer3 = ImageEnhance.Sharpness(im)
  im_output = enhancer3.enhance(1.4)
  im_output.save('passport/ml.jpg')

#   im = Image.open("passport/ml.jpg")
#   #image brightness enhancer
  enhancer = ImageEnhance.Contrast(im)
# # factor = 3.0 #increase contrast
  im_output = enhancer.enhance(factor)
  im_output.save('passport/ml.jpg')  
  image = Image.open("passport/ml.jpg")
  inverted_image = ImageOps.invert(image)
  inverted_image.save('passport/ml.jpg')
        

  result = ocr.ocr("passport/ml.jpg")


  print(len(result[0]));
  try:
    i=0;
    leng=len(result[0]);
    print("RAW DATA :: ",result[0])
    while i<leng:
      temp = result[0][i][1][0];
      if temp[0]=="<" or temp[0]==">":
        print("trash");
      else:
        print(result[0][i][1][0]);
      i+=1;
 
  except:
     print(result[0])




getMrz(path);
print("score :: ",score)