#Spark configuration

from pyspark import SparkConf, SparkContext
appName='myapp'
master='yarn-client'
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)

sc = spark.sparkContext

#.map(func)
lines = sc.parallelize(['hello','world'])
lineLengths = lines.map(lambda s: len(s))
# lineLengths => [5,5]

lines = sc.parallelize(['hello','world'])
chars = lines.flatMap(lambda s: list(s))
# chars => ['h','e','l','l','o','w','o','r','l','d']
