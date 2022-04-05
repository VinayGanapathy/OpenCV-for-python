# -*- coding: utf-8 -*-
"""opencv_4_python_basics_1_reading.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KVCQz1NaEj3QY6irSgjzc8LmgPhp_vi7
"""

# pip install opencv-contrib-python
# pip install caer

# Reading image files using openCV

from google.colab import drive
drive.mount('/content/drive')

import cv2 as cv
from google.colab.patches import cv2_imshow

cat = cv.imread("/content/drive/MyDrive/Colab Notebooks/opencv_for_python/Resources/Photos/cat.jpg")

cv2_imshow(cat)
cv.waitKey(0) 
cv.destroyAllWindows()

cat_large = cv.imread("/content/drive/MyDrive/Colab Notebooks/opencv_for_python/Resources/Photos/cat_large.jpg")

cv2_imshow(cat_large)
cv.waitKey(0) 
cv.destroyAllWindows()

# Reading the videos

capture = cv.VideoCapture("/content/drive/MyDrive/Colab Notebooks/opencv_for_python/Resources/Videos/dog.mp4")

while True:
  isTrue, frame = capture.read()
  cv2_imshow(frame)
 
  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.relaease()
cv.destroyAllWindows()

