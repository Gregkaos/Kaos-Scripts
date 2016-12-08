#!/usr/bin/env python

__description__ = 'Decode Array or Split URL obfucation script'
__author__ = 'Greg Kay'
__version__ = '0.0.7'
__date__ = '2016/11/28'

import optparse
import sys
import string
import re

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

def CreateList(line):
	string=line[line.index("(") + 1:line.rindex(")")]
	list_clean=re.sub(r'[,|_."]', ' ', string)
	return list_clean.split()

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
	t = int(url_list[1])
	while i < 10000:
		if ((h + i) % 104) and ((t + i) % 116) == 0:
			div_h = (h + i) / 104
			break
		i += 1
	for item in url_list:
		sys.stdout.write(chr((int(item) + i) / div_h)) 

def DecodeComboURLDown(url_list):
	i = 1
	h = int(url_list[0])
	t = int(url_list[1])
	while i < 10000:
		if ((h - i) % 104) and ((t + i) % 116) == 0:
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
			url_list = CreateList(line.lower())
		if "split" in line.lower():
			url_list = CreateList(line.lower())
	
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

