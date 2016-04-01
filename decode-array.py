#!/usr/bin/env python

__description__ = 'Decode Array or Split URL obfucation script'
__author__ = 'Greg Kay'
__version__ = '0.0.7'
__date__ = '2016/03/28'

import optparse
import sys
import string
import re

"""
decode-array.py reads from the given file or standard input, and attempts to convert aobfuscated URLs hidden in arrays or splits 
usage examples:   

[user@mypc scripts]$  oledump -s 8 maldoc.vir | ./decode-array.py

http://www.badurl.com/evil.exe

[user@mypc scripts]$ cat bad.txt 

ffGGhh_1 = aRRaY("2449, 2461, 2461, 2457, 2403, 2392, 2392, 2464, 2464, 2464, 2391, 2443, 2442, 2445, 2462, 2459, 2453, 2391, 2444, 2456, 2454, 2392, 2446, 2463, 2450, 2453, 2391, 2446, 2465, 2446")
[user@mypc scripts]$ ./decode-array.py bad.txt 

http://www.badurl.com/evil.exe

For Combo methods two URLs get printed out with one probably looking wrong.  On my ToDo list.
I've never seen one in my analyses, but I'm sure I'll come across it one day.  
If both look wrong but you can recognise a URL format then may need to increase the i value.  ToDo list.


"""

def GetFile(filename):
    try:
        f = open(filename, 'r')
    except:
        return None
    try:
        return f.readlines()
    except:
        return None
    finally:
        f.close()

def GetCleanString(key,line):
	before_key, keyword, after_key = line.partition(key)
	return after_key

def CreateList(new_string):
	words=re.sub(r'[a-zA-Z"(),_|.=]', ' ', new_string).split()
	return words

def IsDivide(i):
	div_h = int(i[0]) % 104
	div_t = int(i[1]) % 116
	if div_h == div_t == 0:
		return int(i[0]) / 104
	else:
		return None

def IsSum(i):
	sum_h = int(i[0]) - 104
	sum_t = int(i[1]) - 116
	if sum_h == sum_t:
		return sum_t
	else:
		return None

def DecodeSumURL(url_list):
	diff = int(url_list[0]) - 104
	for word in url_list:
		sys.stdout.write(chr(int(word) - int(diff)))

def DecodeDivURL(url_list, div):
	for item in url_list:
		sys.stdout.write(chr(int(item) / div))

def DecodeComboURL(url_list):
	i = 1
	h = int(url_list[0])
	while i < 10000:
		if ((h + i) % 104)  == 0:
			div_h = (h + i) / 104
			break
		i += 1
	for item in url_list:
		sys.stdout.write(chr((int(item) + i) / div_h)) 

def DecodeComboURLDown(url_list):
	i = 1
	h = int(url_list[0])
	while i < 10000:
		if ((h - i) % 104)  == 0:
			div_h = (h - i) / 104
			break
		i += 1
	for item in url_list:
		sys.stdout.write(chr((int(item) - 1) / div_h))

def Start(file):
	if file == '':
        	file = sys.stdin.readlines()
	else:
		file = GetFile(file)

	for line in file:
		if "array" in line.lower():
			new_string = GetCleanString("array",line.lower())
		if "split" in line.lower():
			new_string = GetCleanString("split",line.lower())
		
	url_list = CreateList(new_string)
	div = IsDivide(url_list)
	sum = IsSum(url_list)
	
	print '\n'
	if div != None:
		DecodeDivURL(url_list,div)
	if sum != None:
		DecodeSumURL(url_list)
	if div == None and sum == None:
		DecodeComboURL(url_list)
		print "\n"
		DecodeComboURLDown(url_list)
	print '\n'

def Main():
    oParser = optparse.OptionParser(usage='usage: %prog [options] [file]\n' + __description__, version='%prog ' + __version__)
    (options, args) = oParser.parse_args()

    if len(args) == 0:
        Start('')
    else:
        Start(args[0])

if __name__ == '__main__':
	Main()

