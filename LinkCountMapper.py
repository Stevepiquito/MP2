#!/usr/bin/env python
import sys

for line in sys.stdin:
	lsplit = line.split(':')
	SourcePage = lsplit[0].rstrip('\n').strip(' ')
	DestPages = lsplit[1].split(' ')
	print SourcePage.rstrip('\n'),'\t0'
	for f in DestPages:
	  	if f<>'':
			print f.rstrip('\n'),'\t1'


  
