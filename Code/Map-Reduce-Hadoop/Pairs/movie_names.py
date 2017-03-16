#!/usr/bin/env python

import sys

movie_dict={}

movie_file=open('u.item', 'r')

for line in sys.stdin:
  line=line.strip()
  data=line.split('\t')

  for line in movie_file:
    line = line.strip()
    line = line.split('|')
    key = line[0]
    value = line[1]
    movie_dict[key] = value
  
  if data[2]>200:
    try:
      print (movie_dict[data[0]] + "\t" + movie_dict[data[1]] + "\t" + data[2])
    except ValueError:
      pass
