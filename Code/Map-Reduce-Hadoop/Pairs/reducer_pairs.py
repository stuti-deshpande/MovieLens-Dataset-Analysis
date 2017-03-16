#!/usr/bin/env python

import sys

dict1={}


for line in sys.stdin:
  line=line.strip()
  pairs,count=line.split('\t',1)
    
  try:
    count = int(count)
  except ValueError:
    continue

  try:
    dict1[pairs] = dict1[pairs]+count
  except:
    dict1[pairs]=count

  #print dict1
 
for pair in dict1.keys():
  movie1, movie2=pair.split(',',1)
  if dict1[pair]>200:
    print '%s\t%s\t%s'% ( movie1, movie2, dict1[pair] )
  
  
  




  



