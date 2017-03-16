#!/usr/bin/env python

import sys

from collections import defaultdict

dict1={}
movielist=[]
movie_pairs={}
dict2=defaultdict(dict)



for line in sys.stdin:
  line=line.strip()
  data=line.split('\t')

  userID=data[0]
  movieID=data[1]
  rating=data[2]
  rating=int(rating)
  try:
    if rating>=4:
      dict1.setdefault(userID, []).append(movieID)
    else:
      continue
  except ValueError:
    continue

for userID in dict1.keys():
  if len(dict1[userID])>0:
    movielist=list(dict1[userID]) 
    sorted_movielist=sorted(movielist)
    for i in range(0,len(sorted_movielist)):
      for j in range(i + 1,len(sorted_movielist)):
        if i != j:
          if int(sorted_movielist[i]) < int(sorted_movielist[j]):
            pair = str(sorted_movielist[i]).strip(), str(sorted_movielist[j]).strip() 
          else:
            pair = str(sorted_movielist[j]).strip(), str(sorted_movielist[i]).strip() 
         
          if pair in movie_pairs:
            movie_pairs[pair]=movie_pairs[pair]+1
          else: 
            movie_pairs[pair]= 1


for pair in movie_pairs:
  movie1, movie2 = pair[0], pair[1]
  dict2[movie1][movie2]= movie_pairs[pair]

#print dict2
for d in dict2:
  print (str(d)+'\t'+str(dict2[d]))
  