#!/usr/bin/env python
import sys

WordCount = {}
for line in sys.stdin:
	wordsplit = line.split('\t')
	word = wordsplit[0]
	wcount = int(wordsplit[1])
	if word in WordCount:
		WordCount[word] =  WordCount[word]+wcount
	else:
		WordCount[word] =  wcount

for i in WordCount.keys():
	print i,'\t',WordCount[i]
	



