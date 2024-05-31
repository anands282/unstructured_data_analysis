from pyspark.sql import SparkSession

if __name__ = "__main__":
    spark = (SparkSession.builder.appName("unstructured_data_analysis"))
            .config("spark.jars.packages",
                    "org.apache.hadoop:hadoop-aws:3.3.1,")