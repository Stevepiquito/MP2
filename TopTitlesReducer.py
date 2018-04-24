#!/usr/bin/env python
import sys



# input comes from STDIN
for line in sys.stdin:
    w = line.split('\t')
    word = w[0]
    wcount = w[1]
    print word.strip(' ').strip('\n')+'\t'+wcount.strip(' ').rstrip('\n')
 

