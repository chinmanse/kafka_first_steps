from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, avg, count
from pyspark.sql.types import StructType, StringType, FloatType, TimestampType

spark = SparkSession.builder.\
    appname("EcommerceStream").\
    master("local[*]").\
    getOrCreate()

schema = StructType().\
    add('user_id', StringType()).\
    add('action', StringType()).\
    add('product', StringType()).\
    add('price', FloatType()).\
    add('timestamp', StringType())

df = spark.readStream.\
    format('kafka').\
    option('kafka.bootstrap.servers', 'localhost:9092').\
    option('subscribe', 'user_events').\
    load()

events = df.selectExpr('CAST(value AS STRING)').\
    select(from_json(col('value'), schema).alias('data')).\
    select('data.*')

agg = events.groupBy(
    window(col('timestamp'), '1 minute'),
    col('action')
).agg(count('*').alias('total'), avg('price').alias('avg_price'))

query = agg.writeStream.\
    outputMode('update').\
    format('console').\
    start()

query.awaitTerminator()

