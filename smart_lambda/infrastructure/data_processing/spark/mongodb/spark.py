from pyspark.sql import SparkSession

class Spark:

    def __init__(self, name, database):
        return (SparkSession
                    .builder.appName(str(name) if name != None and name != "" else "ingestion-engine_py")
                    .config("spark.mongodb.input.uri", database)
                    .config("spark.mongodb.output.uri", database)
                    .config("hive.exec.dynamic.partition", "true")
                    .config("hive.exec.dynamic.partition.mode", "nonstrict")
                    .enableHiveSupport()
                    .getOrCreate())

    _instance = None

    @staticmethod
    def instance(name, database):
        if Spark._instance == None:
            _instance = Spark(name, database)
        
        return _instance