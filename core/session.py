from pyspark.sql import SparkSession


def build() -> SparkSession:
    spark = (
        SparkSession.builder
        .appName("Local cluster")
        .master("local[*]")

        .config("spark.driver.memory", "4g")
        .config("spark.executor.memory", "4g")
        .config("spark.memory.fraction", "0.7")
        .config("spark.memory.storageFraction", "0.3")

        .config("spark.log.level", "WARN")
        .config("spark.ui.port", "4040")
        .getOrCreate()
    )

    return spark
