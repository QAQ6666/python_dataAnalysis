# -*- coding: utf-8 -*-
from PIL import  Image
import  numpy as np

im = np.array(Image.open('C:/Users/86189/Desktop/sjd.jpg'))
print(im.shape)
print(im.dtype)
print(im)
b = [255, 255, 255] - im
new_im = Image.fromarray(b.astype('uint8'))
new_im.save('C:/Users/86189/Desktop/dbc2.jpg')