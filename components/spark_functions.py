from pyspark.sql import SparkSession
sc = SparkSession.builder
sc = sc.appName("Trieu count app")
sc = sc.master("local")
sc = sc.getOrCreate()

def wordcount(data:str):
    data = list(data.replace('\n', ' ').split(" "))
    words = sc.parallelize(data)
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).collect()
    result = {}
    for r in wordCounts:
        result.update({r[0]:r[1]})
    return result