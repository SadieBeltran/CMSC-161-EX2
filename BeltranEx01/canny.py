import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('darumaka.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,200)
fx = open("x", "w")
fy = open("y", "w")

# https://stackoverflow.com/questions/50274063/find-coordinates-of-a-canny-edge-image-opencv-python
# using canny edge detection, get the edges from the input image
indices = np.where(edges != [0]) #returns a tuple containing the x and y plots
# coordinates = zip(indices[0], indices[1])
indices_len = len(indices[0])
h = img.shape[0]
w = img.shape[1]
j = 0

# increment by 10 so there's fewer points
for i in range(0, indices_len, 10): 
    # write the x and y coordinates into their respective files (to make copy pasting easier)
    fx.write(str(round(indices[0][i]/w,2))+ ",")
    fy.write(str(round(indices[1][i]/h,2))+ ",")
    j+=1
print(j) 

fx.close()
fy.close()