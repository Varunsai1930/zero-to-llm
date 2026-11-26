from PIL import Image
import numpy as np

img = Image.open("./image-np.jpeg")
img_array = np.array(img)
print(img_array)