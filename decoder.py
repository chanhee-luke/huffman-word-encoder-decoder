#/usr/bin/env python
# huffman decoder
# usage: decoder.py key input 

import sys
from bitarray import bitarray

huffman_dict = dict()

try:
	with open(sys.argv[1]) as f:
		for index, line in enumerate(f):
			if index % 2 is 1:
				code = bitarray(line.strip())
				huffman_dict[word] = code
			elif index % 2 is 0:
				word = line.strip()
except IOError:
	print("Cannot open file")
	sys.exit(1)
f.close()

try:
	with open(sys.argv[2]) as file:
		for index, line in enumerate(file):
			code = bitarray(line.strip())
			dec = bitarray(code).decode(huffman_dict)
			output = " ".join(dec)
			print(output.strip('</s>'))
except IOError:
	print("Cannot open file")
	sys.exit(1)
file.close()

