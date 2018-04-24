#!/usr/bin/env python
from operator import itemgetter
import sys

# input comes from STDIN
WordCount = {}
for line in sys.stdin:
	wordsplit = line.split('\t')
	word = wordsplit[0]
	wcount = int(wordsplit[1])
	if word in WordCount:
		WordCount[word] =  WordCount[word]+wcount
	else:
		WordCount[word] =  1
		

for i in WordCount.keys():
	print i,'\t',str(WordCount[i])

