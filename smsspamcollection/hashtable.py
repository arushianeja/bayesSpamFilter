#!/usr/local/bin/python3


import sys, os
import re
import filtering as filt

def create_dictionary(filename):
	hashtable = {}

	with open(filename, 'r') as fp:
		for line in fp:
			words = re.split('\W+', line)

			for ii in range(1,len(words)):
				if words[ii] != '':
					if words[ii] in hashtable:
						hashtable[words[ii]] += 1
					else:
						hashtable[words[ii]] = 1

	return hashtable





def main():
	good = create_dictionary('nonspam.txt')
	bad = create_dictionary('spam.txt')

	probabilty = {}

	# for word in good:
	# 	probabilty[word] = filt.populate_third_dict(good, bad, word, 4827, 747)
	#
	# for word in bad:
	# 	probabilty[word] = filt.populate_third_dict(good, bad, word, 4827, 747)

	
