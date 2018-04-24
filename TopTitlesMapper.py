#!/usr/bin/env python
import sys


WordList = []



for line in sys.stdin:

       w = line.split('\t')
       Word = w[0]
       WCount = int(w[1])
       WordList.append([Word,WCount])	


WordList.sort(key=lambda WordList: WordList[1], reverse=True)
WordListTop = []
i=0
TopItems = 10
while i < TopItems:
	WordListTop.append([WordList[i][0],WordList[i][1]])
	i=i+1

WordListTop.sort(key=lambda WordListTop : WordListTop[0])
i=0
while i < TopItems:
	print WordListTop[i][0],'\t',WordListTop[i][1]
	i=i+1



