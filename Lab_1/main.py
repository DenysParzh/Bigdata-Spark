from pyspark.sql import SparkSession


def main():
    spark = (
        SparkSession.builder
        .appName("Datacamp Pyspark Tutorial")
        .config("spark.memory.offHeap.enabled", "true")
        .config("spark.memory.offHeap.size", "10g")
        .getOrCreate()
    )

    print(spark.sparkContext.appName)


if __name__ == "__main__":
    main()
