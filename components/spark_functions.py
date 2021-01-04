from pyspark import SparkContext
sc = SparkContext("local", "word count url")

def wordcount(data:str):
    data = data.replace('\n', ' ').split(" ")
    words = sc.parallelize(data)
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).collect()
    result = {}
    for r in wordCounts:
        result.update({r[0]:r[1]})
    return result