import sys
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
    prevMovie = None
    dictCoOccurrence = {}
    out = []
    for line in data:
        mov = line.split("\t")
        currMovieID = int(mov.pop(0))
    
        if prevMovie and (prevMovie != currMovieID):
            for key in dictCoOccurrence.keys():
                movieID1, movieID2 = key.split(',')
                output = []
                output.append("%s\t%s" % (movieNameDictionary[int(movieID1)], movieNameDictionary[int(movieID2)]))
                out.append(output)
            dictCoOccurrence = {}
        prevMovie = currMovieID

        #generate the co-occurrence dictionary
        while mov:
            key = str(currMovieID) + "," + str(int(mov[0]))
            if dictCoOccurrence.get(key) == None:
                dictCoOccurrence[key] = 1
            else:
                dictCoOccurrence[key] += 1            
            mov.pop(0)
        
        mov = []

    for key in dictCoOccurrence:
        movieID1, movieID2 = key.split(',')
        output = []
        output.append("%s\t%s" % (movieNameDictionary[int(movieID1)], movieNameDictionary[int(movieID2)]))
        out.append(output)
    return out

conf = SparkConf().setMaster("local[*]").setAppName("Concurrent Matrix")
sc = SparkContext(conf = conf)

text_file = sc.textFile("input/ratings.dat")
movieNameDictionary = loadMovieNames()
out1 = text_file.map(lambda line: line.strip().split("::"))
out2 = out1.filter(lambda a : float(a[2])>4.0)
out3 = out2.map(lambda a : (a[0], a[1])).reduceByKey(lambda x,y : x + ',' + y).map(lambda x: x[1])
out4 = out3.map(lambda line: line.strip().split(",")).map(map1).flatMap(reduce1).map(lambda k: (tuple(k), 1)).reduceByKey(lambda x,y : x+y)
#print(out4.take(100))
out4.saveAsTextFile("input/output")
