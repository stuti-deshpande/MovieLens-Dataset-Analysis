#!/usr/bin/env python

from __future__ import print_function
import sys

dict1={}
movielist=[]



for line in sys.stdin:
  line=line.strip()
  data=line.split('::')

  userID=data[0]
  movieID=data[1]
  rating=data[2]
  rating=float(rating)
  try:
    if rating>=4:
      dict1.setdefault(userID, []).append(movieID)
    else:
      continue
  except ValueError:
    continue
#print dict1

for userID in dict1.keys():
  movielist=list(dict1[userID]) 
  sorted_movielist=sorted(movielist)
  for i in xrange(0,len(sorted_movielist)):
    for j in xrange(i + 1,len(sorted_movielist)):
      if i != j:
        print (str(sorted_movielist[i].strip())+ "," + str(sorted_movielist[j].strip()) + "\t" +"1")