import cv2
#import pytesseract
import PIL.Image

"""
Page segmentation modes:
0 Orientation and script detection (OSD) only
1 Automatic page segmentation with OSD.
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of text.
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possbile in no particulate order.
12 Sparse text with OSD.
12 Raw line. Treat the image as a single text line,
"""

"""
OCR Enginer Mode
0 Legacy engine only
1 Neural nets LSTM engine only
2 Legacy + LSTM engines
3 Default, based on what is available
"""

'''
PLAN OF ACTION: 

- OPEN IMAGE
- adjust area where to process
- THEN process Image
- give all the ingredients

'''
<<<<<<< HEAD

box_config =r"--psm 6 --oem 3"
=======
'''
my_config = r"--psm 6 --oem 3"
box_config =r"--psm 12 --oem 3"
>>>>>>> a3e2e0a32b86bbc7b9fc40e3dfe23c7e2b5dc2d4


box_text = pytesseract.image_to_string(PIL.Image.open("test.png"), config =box_config)
cookiess_text = pytesseract.image_to_string(PIL.Image.open("cookiess.png"), config = box_config)

ingredients_list_pre = cookiess_text.split(" ")

ingredients_list_after = list()

remove = [ "%", "!", "@", "#",  "&", "(", ")", "_", "+", "-", "=", "0", "\n"]

for i in range(len(ingredients_list_pre) - 1):
    if ingredients_list_pre[i] not in remove:
        ingredients_list_after.append(ingredients_list_pre[i])
    if len(ingredients_list_pre[i]) > 3:
        ingredients_list_after.append(ingredients_list_pre[i])


<<<<<<< HEAD

print(ingredients_list_after)
=======
print(box_text)
'''

halal_ingredients = []

haram_ingredients = []
>>>>>>> a3e2e0a32b86bbc7b9fc40e3dfe23c7e2b5dc2d4

