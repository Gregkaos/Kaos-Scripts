#!/usr/bin/env python

__description__ = 'Create obsfucated URL using additions or multipliers'
__author__ = 'Greg Kaos'
__version__ = '0.0.2'

add_array=[]
mult_array=[]

url_in=raw_input('URL: ')
add_in=raw_input('Add: ')
mul_in=raw_input('Mult: ')

for i in url_in:
	add_array.append(ord(i) + int(add_in))
	mult_array.append(ord(i) * int(mul_in))

f_a = open('a.txt', 'w')
f_b = open('b.txt', 'w')

f_a.write('addition = ArRaY(' + str(add_array).strip('[] ') + ')')
f_b.write('multiply = aRRaY(' + str(mult_array).strip('[] ') + ')')

print ('addition = ArRaY(' + str(add_array).strip('[] ') + ')')
print ('\nmultiply = aRRaY(' + str(mult_array).strip('[] ') + ')')

f_a.close()
f_b.close()

