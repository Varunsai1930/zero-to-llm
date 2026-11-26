### Every Day Workdone

#### Date: 24th Nov 2026
Watched Keith Galli — Complete Python NumPy Tutorial (~1h) and practiced some of the work

How to load an image as a NumPy array

##### Code:

from PIL import Image
import numpy as np

img = Image.open("./image-np.jpeg")
img_array = np.array(img)
print(img_array)
