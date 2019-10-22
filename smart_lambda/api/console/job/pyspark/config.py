from py4j.java_gateway import JavaGateway

class Config:

    _CONFIG_TABLE = "ingestion:properties"

    def __init__(self, key):
        self.name = "ingestion-engine"
        self.key = key
        self.domain_settings = DataDomainSettings(key)

    _instance = None

    @staticmethod
    def instance(key):
        if Config._instance == None:
            _instance = Config(key)
        return _instance

class HiveSettings:
    def __init__(self, properties):
        self.name = "HIVE"
        self.table = "raw_site.example"
        self.savemode = "append"
        self.partition = "date"
        self.partitiontype = "date"
        self.location = "hdfs://vvdataprdnnha/raw/site/example"
        #self.name = properties.hive.name
        #self.table = properties.hive.table
        #self.savemode = properties.hive.savemode
        #self.partition = properties.hive.partition
        #self.partitiontype = properties.hive.partitiontype
        #self.location = properties.hive.location

#put 'ingestion:properties', 'PTO_ATV_IPL-LOJA', 'config:dataBaseHive','raw_loja'        

class MongoDBSettings:
    def __init__(self, properties):
        self.name = "MONGODB"
        self.connection = "mongodb://emp_ingestion:3vv4Mk1P14c3@bd-mongodb001.prd.bigdata.dc.nova,bd-mongodb002.prd.bigdata.dc.nova,bd-mongodb003.prd.bigdata.dc.nova/evvamktplace.example_temp"
        self.savemode = "overwrite"
        self.partition = "date"
        self.partitiontype = "date"
        #self.name = properties.mongodb.name
        #self.connection = properties.mongodb.connection
        #self.savemode = properties.mongodb.savemode
        #self.partition = properties.mongodb.partition
        #self.partitiontype = properties.mongodb.partitiontype

class KafkaSettings:
    def __init__(self, properties):
        self.name = "KAFKA"
        bootstrap_servers=['localhost:9092']
        self.topic = "example"
        self.savemode = "append"
        self.partition = "date"
        self.partitiontype = "date"
        #self.name = properties.kafka.name
        #self.connection = properties.kafka.connection
        #self.savemode = properties.kafka.savemode
        #self.partition = properties.kafka.partition
        #self.partitiontype = properties.kafka.partitiontype        

class DataDomainSettings:
    def __init__(self, key):
        self.mongodb_settings = MongoDBSettings(None)
        self.hive_settings = HiveSettings(None)
        self.kafka_settings = KafkaSettings(None)
        self.source = self.mongodb_settings
        self.destination = self.hive_settings

        # gateway = JavaGateway()
        # hbase_config = gateway.jvm.br.com.vvdatalab.controller.ControllerConfig()
        # properties = hbase_config.getAllFieldsHbase(_CONFIG_TABLE, key)

        # self.mongodb_settings = MongoSettings(properties.mongo)
        # self.hive_settings = HiveSettings(properties.hive)
        # self.source = self._get_data_source()
        # self.destination = self._get_data_destination()

    def _get_data_source(self, properties):
        return self.mongodb_settings if properties.source.upper() == "MONGODB" else self.hive_settings

    def _get_data_destination(self, properties):
        return self.mongodb_settings if properties.source.upper() == "MONGODB" else self.hive_settings

# mongodb://emp_ingestion:3vv4Mk1P14c3@bd-mongodb001.prd.bigdata.dc.nova,bd-mongodb002.prd.bigdata.dc.nova,bd-mongodb003.prd.bigdata.dc.nova/evvamktplace.evva_market_place_pedido_temp
# mongodb://127.0.0.1:27017
#"mongodb://svc_bigdata:l7%uRyZ.Arvz:6FB13d@@mdbp-cb-1,mdbp-cb-2,mdbp-cb-3,mdbp-cb-4/db_prd_casasbahia"
#"mongodb://svc_bigdata:l7%uRyZ.Arvz:6FB13d@@mdbp-cb-1,mdbp-cb-2,mdbp-cb-3,mdbp-cb-4/db_prd_pontofrio"