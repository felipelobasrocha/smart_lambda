from pyspark.sql import SparkSession

class Spark:

    session = None
    action = None

    def __init__(self, name):
        self.session = SparkSession.builder.appName(name)\
                                    .config("hive.exec.dynamic.partition", "true")\
                                    .config("hive.exec.dynamic.partition.mode", "nonstrict")\
                                    .enableHiveSupport()\
                                    .getOrCreate()

    _instance = None

    @staticmethod
    def instance(name):
        if Spark._instance == None:
            _instance = Spark(name)
        
        return _instance
