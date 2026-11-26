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

#### Date: 25th Nov 2026

Watched the same keith galli numpy video again, and did some of the exercises in the video

solved a problem from the video - prob.py

one = np.ones((5,5))
zero = np.zeros((3,3))
zero[1,1] = 9
one[1:4,1:4] = zero
print(one)


another problem is added to prob2.py