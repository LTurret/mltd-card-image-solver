import cv2 as cv
import numpy as np
import os

images = {}
cv_images = []
axis = [1, 1, 0, 1, 0]

path_prefix = "./images/Sprite"
output_path = "./build/"

if not os.path.isdir(output_path):
    os.mkdir(output_path)

output_path += f"{os.path.basename(os.listdir(path_prefix)[0][:-6])}.png"

for counter, directory in enumerate(os.listdir(path_prefix)):
    with open(f"{path_prefix}/{directory}", "rb") as image:
        images[
            f"image{len(os.listdir(path_prefix))-counter-1}"
        ] = f"{path_prefix}/{directory}"

for image in images:
    cv_images.append(cv.imread(images[image], cv.IMREAD_UNCHANGED))

merged_image = cv_images[-1]
for counter, i in enumerate(range(2, len(cv_images) + 1)):
    merged_image = np.concatenate(
        (cv_images[len(images) - i], merged_image), axis=axis[counter]
    )
cv.imwrite(output_path, merged_image)
