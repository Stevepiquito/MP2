#!/usr/bin/env python
import sys

Top = []
Sum = 0
Max = 0
Min = 99999
Numbers = []
for line in sys.stdin:
    Entry = line.split('\t')
    Word = Entry[0]
    Count = int(Entry[1])
    Top.append([Word,Count])
    Sum = Sum + Count
    Max = max(Count, Max)
    Min = min(Count,Min)
    Numbers.append(Count)
Avg = int(Sum / 10)
temp = 0
for i in Numbers:
   temp = temp +  ((i-Avg)*(i - Avg))
Var = int(temp  / 10)
print 'Mean\t',Avg
print 'Sum\t',Sum
print 'Min\t',Min
print 'Max\t',Max
print 'Var\t',Var


