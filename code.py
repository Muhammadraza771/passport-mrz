# import joblib
# import PIL
# import easyocr
# import sys
# import cv2
# from PIL import Image as im
# import numpy as np


# #loading the ML model (mod.joblib)

# filename = "mod.joblib"
# model = joblib.load(filename)


# #getting the list of images from backend javascript
# itemList = sys.argv[1]; 
# my_list = itemList.split(",")



# #cropping images for mrz only

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

#     print(extractMrz(mrz_area))


# def extractMrz(cropped_image):
#     temp = im.fromarray(cropped_image)
#     temp.save("pImages/mlImage.jpg")
#     result = model.readtext("pImages/mlImage.jpg", detail=0)
#     mrz_concat=""
#     for x in result:
#       mrz_concat +=x
#     mrz_concat=mrz_concat.replace(" ","")
#     return mrz_concat; 




# # crop_mrz_area("pImages/1 (11).jpg")


# for x in my_list:
#   crop_mrz_area("pImages/"+x)










 


# # # print(type("C:\Users\Personal PC\Desktop\test\nineteen.jpg"))

# # print("Image Type ",type("C:/Users/Personal PC/Desktop/test/nineteen.jpg"));

# # temp = model.readtext(imgPath, detail=0)



# # # print(type(loaded_model));