from __future__ import division
from PIL import Image
from PIL import ImageOps
from time import sleep
import numpy

# y = Image.open('triangles.png')
# pix = numpy.array(y)
# print len(pix[0])
# pix = list(pix)
# for i in range(len(pix)):
# 	for j in range(len(pix[0])):
# 		print i,j, pix[i][j]

# import numpy as np
# P=2.45
# S=[22, 33, 45.6, 21.6, 51.8]
# SP = P*np.array(S)
# print SP


# # pixels = list(new_im.getdata())

# def get_bounds(obj):
# 	obj = obj.load()

# 	index = 0
# 	first = 0
# 	second = 0
# 	while True:
# 		try: 
# 			x = obj[index,0]
# 		except IndexError:
# 			first = index
# 			break
# 		index += 1

# 	index = 0
# 	while True:
# 		try: 
# 			x = obj[0,index]
# 		except IndexError:
# 			second = index
# 			break
# 		index += 1
# 	return first,second


# #The unblurred image 
# x = Image.open('road.png')
# y = ImageOps.expand(x,border=1,fill='red')
# y.save('test.png')

# new_im = Image.open('test.png')
# ni_pixels = new_im.load()# create the pixel map

# #Instantiate the blurred image as an all black image that's the same size as the old image plus the border
# blurred_image = Image.new('RGB', (new_im.size[0],new_im.size[1]), "black") #create a new black image
# blurred_image_pixels = blurred_image.load()

# for i in range(1, blurred_image.size[0]-1):
# 	for j in range(1, blurred_image.size[1]-1):

# 		top = ni_pixels[i-1,j][0]
# 		bot = ni_pixels[i+1,j][0]
# 		left = ni_pixels[i,j-1][0]
# 		right = ni_pixels[i,j+1][0]
# 		top_bottom_left_right = 2*(top + bot + left + right)
	
# 		bot_right = ni_pixels[i+1,j+1][0]
# 		bot_left = ni_piels[i+1,j-1][0]
# 		top_right = ni_pixels[i-1,j+1][0]
# 		top_left = ni_pixels[i-1,j-1][0]
# 		corners = bot_right + bot_left + top_right + top_left

# 		new_value = ((top_bottom_left_right + corners) + (3*(ni_pixels[i,j][0])))/15
# 		blurred_image_pixels[i,j] = (int(new_value),int(new_value),int(new_value))

# blurred_image = ImageOps.crop(blurred_image, border=1)
# blurred_image.save('blurred_image.png')


#### numpy.subtract(guess_image, (numpy.multiply(2, Gauss(numpy.subtract(first,Gauss(guess_image))))))
# alpha = 2
# first = numpy.array(Image.open('blurred_image.png'))
# guess_image = numpy.empty_like (first)
# guess_image[:] = first

# inner_term = numpy.subtract(first,Gauss(guess_image))
# outer_term = Gauss(inner_term)
# derivative = numpy.multiply(2, outer_term)
# derivative = zero(derivative)
# guess_image = numpy.subtract(guess_image, derivative)
# guess_image = numpy.multiply(alpha, guess_image)