from __future__ import division
from PIL import Image
from PIL import ImageOps
from time import sleep
import numpy
import copy

def Gauss(array):
	larger_array = numpy.zeros(shape=(len(array)+2,len(array[0])+2), dtype=object)

	for i in range(1,len(array)+1):#weird
		for j in range(1,len(array[0])+1):
			larger_array[i][j]=array[i-1][j-1][0]

	for i in range(1, len(larger_array)-1):
		for j in range(1,len(larger_array[0])-1):
			top = larger_array[i-1][j]
			bot = larger_array[i+1][j]
			left = larger_array[i][j-1]
			right = larger_array[i][j+1]
			top_bottom_left_right = 2*(int(top) + int(bot) + int(left) + int(right))
		
			bot_right = larger_array[i+1][j+1]
			bot_left = larger_array[i+1][j-1]
			top_right = larger_array[i-1][j+1]
			top_left = larger_array[i-1][j-1]
			corners = int(bot_right) + int(bot_left) + int(top_right) + int(top_left)

			new_value = ((top_bottom_left_right + corners) + (3*int(larger_array[i,j])))/15
			array[i-1][j-1] = (int(new_value),int(new_value),int(new_value))
	return array

sharp_image = Image.open('squares.png')
sharp_image_matrix = numpy.array(sharp_image)
for i in range(1):
	sharp_image_matrix = Gauss(sharp_image_matrix)
blurred_image = Image.fromarray(sharp_image_matrix)
blurred_image.save('blurred_image.png')

alpha = 1
first = numpy.array(Image.open('blurred_image.png'))
guess_image = numpy.empty_like(first)
guess_image[:] = first