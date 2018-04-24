#!/usr/bin/env python
import sys


for line in sys.stdin:
    w = line.split('\t')
    word = w[0]
    wcount = w[1]
    print word.strip(' ')+'\t'+wcount.strip(' ').rstrip('\n')
