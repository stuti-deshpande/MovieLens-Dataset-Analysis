

import sys
from operator import add
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import itertools

def loadMovieNames():
  movieNames = {}
  with open("input/u.item") as f:
    for line in f:
      fields = line.split("|")
      movieNames[int(fields[0])] = fields[1].decode('ascii', 'ignore')
  return movieNames

def map1(data):
  arr = []
  while data:
    arr.append('\t'.join(data))
    data.pop(0)
  return arr

def reduce1(data):
  for line in data:
    line=line.split('\t')

    dict1=line(dict)
    dict2={}
    for userID in dict1.keys():
    movielist=list(dict1[userID]) 
    sorted_movielist=sorted(movielist)
    for i in xrange(0,len(sorted_movielist)):
      for j in xrange(i + 1,len(sorted_movielist)):
        if i != j:
          dict2={((str(sorted_movielist[i].strip())+ "," + str(sorted_movielist[j].strip())), "1")}

    try:
      dict2[pairs] = dict2[pairs]+count
    except:
      dict2[pairs]=count
    for pair in dict2.keys():
      movie1, movie2=pair.split(',',1)
        
  return dict2 


conf = SparkConf().setMaster("local[*]").setAppName("Cooccurrence_Stripes")
sc= SparkContext(conf=conf)

text_file=sc.textFile("input/u.data")
out1=text_file.map(lambda line: line.strip().split("\t"))
out2=out1.filter(lambda a: float(a[2])>4.0)
out3=out2.filter(lambda a: (a[0],a[1])).reduceByKey(lambda x,y : x + ',' + y).map(lambda x: x[1])
out4 = out3.map(lambda line: line.strip().split(",")).map(map1).flatMap(reduce1).map(lambda k: (tuple(k), 1)).reduceByKey(lambda x,y : x+y)
print (out3.take(5))