class DDLCommand:

    def __init__(self):
        self.CREATE_TABLE = "CREATE EXTERNAL TABLE IF NOT EXISTS REPLACETABLE REPLACECOLUMN \
                    PARTITIONED BY (REPLACEPARTITION) \
                    ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.orc.OrcSerde' \
                    STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat' \
                    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat' \
                    LOCATION 'REPLACELOCATION' \
                    TBLPROPERTIES ( \
                    'orc.compress'='ZLIB', \
                    'transient_lastDdlTime'='1561471323')"