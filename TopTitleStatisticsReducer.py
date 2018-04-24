#!/usr/bin/env python
import sys



Results = {}

for line in sys.stdin:
     lStrip = line.split('\t')
     Results[lStrip[0]]=lStrip[1]	

#TODO
print 'Mean\t',Results['Mean'].rstrip('\n')
print 'Sum\t',Results['Sum'].rstrip('\n')
print 'Min\t',Results['Min'].rstrip('\n')
print 'Max\t',Results['Max'].rstrip('\n')
print 'Var\t',Results['Var'].rstrip('\n')


