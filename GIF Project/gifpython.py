# Basic Python: Final Project - Creating a GIF

import imageio.v3 as iio

filenames = ["IMG_0777.PNG", "IMG_0781.PNG", "IMG_0780.PNG"]
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("hipom.gif", images, duration=500, loop=0)
