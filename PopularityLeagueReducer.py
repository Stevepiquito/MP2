#!/usr/bin/env python
import sys
LeagueList = []

# input comes from STDIN
for line in sys.stdin:
    lsplit = line.split('\t')
    LeagueList.append([lsplit[0].strip(''),int(lsplit[1].strip('').rstrip('\n'))]) 	


LeagueList.sort(key=lambda LeagueList: LeagueList[1])
LPop = []
i = 0
j = 1
Last = -1
for f in LeagueList:
	if  (int(f[1])==int(Last)):	
		LPop.append([f[0],i-j])
		j = j +1
		Last = f[1]
		i = i+1
	else:
		LPop.append([f[0],i])
		i = i +1
		j = 1
		Last = f[1]	

LPop.sort(key=lambda LeagueList: LeagueList[0], reverse = True)
for f in LPop:
	print f[0].strip(' ')+'\t'+str(f[1]).strip(' ')
        #print int(f[0]),'\t',int(f[1])


 
