from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KafkaToHDFS:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("KafkaToHDFS") \
            .config("spark.sql.adaptive.enabled", "true") \
            .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
            .getOrCreate()
        
        self.spark.sparkContext.setLogLevel("WARN")
        
    def define_schema(self):
        """Define el esquema para los datos de ventas"""
        return StructType([
            StructField("transaction_id", StringType(), True),
            StructField("product", StringType(), True),
            StructField("quantity", IntegerType(), True),
            StructField("price", DoubleType(), True),
            StructField("region", StringType(), True),
            StructField("timestamp", StringType(), True),
            StructField("customer_id", StringType(), True)
        ])
    
    def start_streaming(self):
        """Inicia el streaming desde Kafka a HDFS"""
        try:
            # Leer stream desde Kafka
            df = self.spark \
                .readStream \
                .format("kafka") \
                .option("kafka.bootstrap.servers", "localhost:9092") \
                .option("subscribe", "sales-data") \
                .option("startingOffsets", "latest") \
                .load()
            
            # Convertir valores de bytes a string
            json_df = df.select(
                col("key").cast("string"),
                from_json(col("value").cast("string"), self.define_schema()).alias("data")
            ).select("data.*")
            
            # Procesar datos - agregar columna de fecha para particionado
            processed_df = json_df.withColumn(
                "processing_timestamp", current_timestamp()
            ).withColumn(
                "date", to_date(col("timestamp"))
            ).withColumn(
                "total_sale", col("quantity") * col("price")
            )
            
            # Escribir a HDFS en formato Parquet
            query = processed_df.writeStream \
                .outputMode("append") \
                .format("parquet") \
                .option("path", "hdfs://namenode:9000/data/sales/raw") \
                .option("checkpointLocation", "hdfs://namenode:9000/checkpoints/sales") \
                .option("truncate", "false") \
                .partitionBy("date") \
                .trigger(processingTime="60 seconds") \
                .start()
            
            logger.info("Streaming iniciado...")
            query.awaitTermination()
            
        except Exception as e:
            logger.error(f"Error en el streaming: {e}")
        finally:
            self.spark.stop()

if __name__ == "__main__":
    stream_processor = KafkaToHDFS()
    stream_processor.start_streaming()