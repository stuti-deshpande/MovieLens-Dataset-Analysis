#!/usr/bin/env python2.6

from operator import itemgetter
import sys
import ast
import operator

dict1 = {} 
movie = None

for line in sys.stdin:

    line=line.strip()
    movie, movie_stripe = line.split('\t', 1)

    #movie_stripe=movie_stripe.findall(r'"\s*([^"]*?)\s*"', movie_stripe)
     
    movie_stripe = ast.literal_eval(movie_stripe)
 
    movie_stripe = dict(movie_stripe)
   
    
    for k in movie_stripe:
	  if int(movie) < int(k):
	    new_moviepair  = str(movie) + ' ' + str(k)
	  else:
		new_moviepair = str(k) + ' ' + str(movie)
        
	  if new_moviepair in dict1:
		dict1[new_moviepair] += movie_stripe[k]
	  else:
		dict1[new_moviepair] = movie_stripe[k]

for d in dict1:
	movie1, movie2 = d.split()
	if dict1[d]>200:	
	  print movie1, movie2, dict1[d]