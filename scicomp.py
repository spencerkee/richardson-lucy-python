from __future__ import division
from PIL import Image
from PIL import ImageOps
from time import sleep
import numpy
import copy

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

y = Image.open('squares.png')
pix = numpy.array(y)
for i in range(1):
	pix = Gauss(pix)
blurred_image = Image.fromarray(Gauss(pix))
blurred_image.save('blurred_image.png')

# numpy.subtract(guess_image, (numpy.multiply(2, Gauss(numpy.subtract(first,Gauss(guess_image))))))
alpha = 1
first = numpy.array(Image.open('blurred_image.png'))
guess_image = numpy.empty_like(first)
guess_image[:] = first

# x = numpy.empty_like(first)
# x = first[:]

numpy.seterr(divide='ignore')

def subtract_matricies(m1, m2):
	return_matrix = copy.deepcopy(m1)
	for i in range(len(m1)):
		for j in range(len(m1[0])):
			print m1[i][j], m2[i][j], (m1[i][j] - m2[i][j])
			return_matrix[i][j] = (m1[i][j] - m2[i][j])
	return return_matrix

for i in range(1):
	inner_term = numpy.subtract(first,Gauss(guess_image))
	# inner_term = subtract_matricies(first,Gauss(first))

	# print first == Gauss(first)

	asdf = Gauss(first)
	test = Image.fromarray(asdf)
	# test = Image.fromarray(first)
	test.save('test.png')


	# for i in inner_term:
	# 	print i2

	# outer_term = Gauss(inner_term)

	# for i in inner_term:
	# 	print i




# 	for i in range(len(first)):
# 		for j in range(len(first[0])):
# 			print 'first',first[i][j], 'guess',x[i][j], inner_term[i][j]

# 	# print inner_term[0][0]




	# derivative = numpy.multiply(2, outer_term)



# 	# derivative = outer_term	


# 	# derivative = zero(derivative)



# 	guess_image = numpy.subtract(guess_image, derivative)
# 	# guess_image = numpy.multiply(alpha, guess_image)
# guess_image = Image.fromarray(guess_image)
# guess_image.save('guess_image.png')

# # print first == x

