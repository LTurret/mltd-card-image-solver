import cv2 as cv
import numpy as np
import os

images = {}
cv_images = []
linked_images = []
axis = [1, 1, 0, 1, 0]

path_prefix = "./testing"

for counter, directory in enumerate(os.listdir(path_prefix)):
    with open(f"{path_prefix}/{directory}", "rb") as image:
        images[f"image{len(os.listdir(path_prefix))-counter-1}"] = f"{path_prefix}/{directory}"

print(images)

for image in images:
    cv_images.append(cv.imread(images[image], cv.IMREAD_UNCHANGED))

def process():
    new_image = cv_images[-1]
    new_image = np.concatenate((cv_images[len(images)-2], new_image), axis=1)

    cv.namedWindow("image", 0)
    cv.imshow("image", new_image)
    cv.waitKey(0)
    cv.destroyWindow("image")

process()