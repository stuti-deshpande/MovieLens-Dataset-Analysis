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

def map1(inp):
    out = []
    for line in inp:
        out.append(line + "\t" + "1")
        out.append(line + "\t" + "*")
    return out

def red1(inp):
    totalMov1 = 0
    total = 0
    prevKey = False
    out = []
    tt = 0
    for line in inp:
        tt += 1
        line = line.strip()
        data = line.split("\t")
        currentKey = '\t'.join(data[:2])
        count = 1
    
        if prevKey and currentKey != prevKey: 
            if data[2] != "*":
                condProb = 0
                lift = 0
                if totalMov1 != 0:
                    condProb = float(total)/totalMov1
                    lift =float(condProb)/totalMov1
                if lift > 1.6:
                    out.append(prevKey + "\t" + '%0.10f' % float(lift))
            else: # Special key encountered
                totalMov1 = total
            prevKey = currentKey
            total += 1
        else:
            prevKey = currentKey
            total += 1

# emit last key
    if prevKey:
        condProb = 0
        lift = 0
        if totalMov1 != 0:
            condProb = float(total)/totalMov1
            lift = float(condProb)/totalMov1
        if condProb > 1.6:
            out.append(prevKey + "\t" + '%0.10f' % float(lift))
    return out

conf = SparkConf().setMaster("local[*]").setAppName("Concurrent Matrix")
sc = SparkContext(conf = conf)

text_file = sc.textFile("input/u.data")
movieNameDictionary = loadMovieNames()
out1 = text_file.map(lambda line: line.strip().split("\t"))
out2 = out1.filter(lambda a : float(a[2])>4.0)
out3 = out2.map(lambda a : (a[0], a[1])).reduceByKey(lambda x,y : x + ',' + y).map(lambda x: x[1]).map(lambda line: line.strip().split(",")).map(lambda words : list(map('\t'.join, itertools.combinations(words, 2)))).map(map1).map(red1)
print(out3.take(10))
#out4.saveAsTextFile("input/output")

