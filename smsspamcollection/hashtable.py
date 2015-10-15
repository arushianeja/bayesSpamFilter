#!/usr/local/bin/python3


import sys, os
import re

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
