#!/usr/bin/env python

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


delimitersList = []
with open(stopWordsPath) as f:
    stopWordsList = f.readlines()



stopWordsListLower = []
for i in stopWordsList:
	stopWordsListLower.append(i.lower()) 

with open(delimitersPath) as f:
    delimiters = f.read()
    for x in delimiters:
	delimitersList.append(x)

for line in sys.stdin:

    x=0
    lineW = []
    lineW.append(line)
    while x <len(delimiters):
	lines_split = []
	for w in lineW:
		r = w.split(delimiters[x])			  
		for i in r:
			lines_split.append(i.rstrip('\n'))
   	lineW = lines_split
	x = x+1


    for x in lineW:
		xl = x.lower().strip()
		flag = 0
    		for y in stopWordsListLower:
       		 	if ((xl == y.strip()) or (xl =='')):
				flag = 1
		if flag == 0:
			print xl,'\t 1'	   

