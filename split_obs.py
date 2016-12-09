#!/usr/bin/env python

__description__ = 'Create obsfucated split URLs Addition - c.txt Multiplier d.txt'
__author__ = 'Greg Kaos'
__version__ = '0.0.2'

import re

add_array=[]
mult_array=[]

url_in=raw_input('URL: ')
add_in=raw_input('Add: ')
mul_in=raw_input('Mult: ')
delim_in=raw_input('Split Delim: ')

for i in url_in:
	add_array.append(ord(i) + int(add_in))
	mult_array.append(ord(i) * int(mul_in))

tmp_add = re.sub(r', ', delim_in,str(add_array).strip('[] '))
tmp_mult = re.sub(r', ', delim_in,str(mult_array).strip('[] '))

f_a = open('c.txt', 'w')
f_b = open('d.txt', 'w')

f_a.write('addition = spLIt(' + tmp_add + ', %s)'%str(delim_in)) 
f_b.write('multiply = SPlIT(' + tmp_mult + ', %s)'%str(delim_in)) 

print ('addition = spLIt(' + tmp_add + ', %s)'%str(delim_in)) 
print ('\nmultiply = SPlIT(' + tmp_mult + ', %s)'%str(delim_in))

f_a.close()
f_b.close()
