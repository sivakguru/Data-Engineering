from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, Catalog

spark_conf = SparkConf()
spark_conf.setAll([
    ('spark.master', 'spark://10.6.9.252:7077'),
    ('spark.app.name', 'myApp'),
    ('spark.submit.deployMode', 'client'),
    ('spark.ui.showConsoleProgress', 'true'),
    ('spark.eventLog.enabled', 'false'),
    ('spark.logConf', 'false'),
    ('spark.driver.bindAddress', '0.0.0.0'),
    ('spark.driver.host', '10.6.9.252')
])

spark          = SparkSession.builder.config(conf=spark_conf).getOrCreate()
spark_ctxt          = spark_sess.sparkContext
spark_reader        = spark_sess.read
spark_streamReader  = spark_sess.readStream
spark_ctxt.setLogLevel("WARN")

air_q_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://10.6.9.252:5432/ccs_postgre") \
    .option("dbtable", "public.air_quality_index") \
    .option("user", "skumar763") \
    .option("password", "Skumar@763") \
    .option("driver", "org.postgresql.Driver") \
    .load()