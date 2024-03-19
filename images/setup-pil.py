import os
from PIL import Image

def convert_images():
    while x < 6:
        im = Image.open("neo.png")
        #get image size (width, height)
        image_size = im.size
        print("Uploaded image Width = {}, Height = {}".format(image_size[0], image_size[1]))
        new_im = im.resize((480,300))
        new_im.save("example_resized-{}.png".format(x))
        x = x + 1


""" print("New image Width = {}, Height = {}".format(new_im.size[0], new_im.size[1]))
print("New image is saved to", path_to_new_image) """
