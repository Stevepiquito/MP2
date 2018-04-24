#!/usr/bin/env python
import sys


leaguePath = sys.argv[1]
LeagueList = []
Pages = []

with open(leaguePath) as f:
	LeagueList = f.readlines()

for line in sys.stdin:
	lsplit = line.split('\t')
	Page = lsplit[0].rstrip('\n').strip(' ')
	PageCount = int(lsplit[1])
	Pages.append([Page,PageCount])
	for f in LeagueList:
	  	if int(f)==int(Page):
			print Page.rstrip('\n'),'\t',PageCount

