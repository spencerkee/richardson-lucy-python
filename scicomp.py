from __future__ import division
from PIL import Image
from PIL import ImageOps
from time import sleep
import numpy

y = Image.open('road.png')
pix = numpy.array(y)

def zero(array):
	for i in range(len(array)):
		for j in range(len(array[0])):
			if array[i][j][0] < 0:
				array[i][j] = [0, 0, 0]
	return array

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

x = Image.fromarray(Gauss(pix))
# x.show()

#### numpy.subtract(guess_image, (numpy.multiply(2, Gauss(numpy.subtract(first,Gauss(guess_image))))))
alpha = 2
first = numpy.array(Image.open('triangles.png'))
guess_image = numpy.empty_like(first)
guess_image[:] = first

inner_term = numpy.subtract(first,Gauss(guess_image))
outer_term = Gauss(inner_term)
derivative = numpy.multiply(2, outer_term)
derivative = zero(derivative)
guess_image = numpy.subtract(guess_image, derivative)
guess_image = numpy.multiply(alpha, guess_image)
x = Image.fromarray(guess_image)
x.show()