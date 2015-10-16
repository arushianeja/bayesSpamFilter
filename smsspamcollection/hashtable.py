#!/usr/local/bin/python3


import sys, os
import re
import filtering as filt
import numpy as np

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





def main(argv):
	good = create_dictionary('nonspam.txt')
	bad = create_dictionary('spam.txt')

	# Read one line from the standard input.
	line = sys.stdin.readline()

	# Split it in words.
	words = re.split('\W+', line)

	# Start with a numpy array of zeros.
	probv = np.zeros(len(words))
	kk = 0

	# Not sure if this is the right thing to do. I'm not considering the chance
	# of the same word occurring more than once. If that happens, the probabilty
	# will just occur multiple times in the prodv array.
	for ii in range(len(words)):
		# Only calculate the probabilty of non-empty strings.
		if words[ii] != '':
			probv[kk] = filt.populate_third_dict(good,bad,words[ii],4827,747)
			kk += 1

	# Let's crop the array to account only for the non-empty words.
	probv = probv[:kk]

	# This is the function we couldn't decypher last night (I think!).
	spamprob = probv.prod() / (probv.prod()+(1-probv).prod())

	if spamprob > 0.9:
		print('It\'s spam!')
	else:
		print('It\'s legit!')

	# for word in good:
	# 	probabilty[word] = filt.populate_third_dict(good, bad, word, 4827, 747)
	#
	# for word in bad:
	# 	probabilty[word] = filt.populate_third_dict(good, bad, word, 4827, 747)


if __name__ == '__main__':
	main(sys.argv[1:])
