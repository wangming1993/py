from skimage import data,io

from skimage.color import rgb2gray
from skimage import data

img = data.astronaut()
img_gray = rgb2gray(img)