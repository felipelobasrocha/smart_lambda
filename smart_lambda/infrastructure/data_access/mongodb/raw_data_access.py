from pyspark.sql.functions import unix_timestamp, lit, date_format

from smart_lambda.infrastructure.data_access.contracts.iraw_data_access import IRawDataAccess

class RawDataAccess(IRawDataAccess):

    _DATE_FORMAT = "y-M-d"
    _DATE_TYPE = "date"
    _INT_TYPE = "int"

    def __init__(self, data_settings):
        self._data_settings = data_settings

    def get(self, partition_value=None):
        data = (self._data_settings.spark.session.read
                                    .format("com.mongodb.spark.sql.DefaultSource")
                                    .option("uri", self._data_settings.mongodb_settings.connection)
                                    .load()
                )
        if partition_value != None:
            data = self._filter_by_partition(data, partition_value)
        return data

    def save(self, domain_event, action):
        action(domain_event.domain, self.data_settings.mongodb_settings)        

    def raise_event(self, event, data_domain, callback):
        try:
            domain_event = event(data_domain)
            return self.save(domain_event, callback)
        except Exception as e:
            print "MongodbRawDataAccess error:" + str(e)

    def _filter_by_partition(self, data, partition_value):
        if self._data_settings.mongodb_settings.partitiontype == self._DATE_TYPE:
            return (data.where(date_format(lit(data[self._data_settings.mongodb_settings.partition]), self._DATE_FORMAT) == 
                                date_format(lit(partition_value), self._DATE_FORMAT)
                            ))
        elif self._data_settings.mongodb_settings.partitiontype == self._INT_TYPE:
            return data.where(data[self._data_settings.mongodb_settings.partition] == partition_value)
        else:
            return data.where(data[self._data_settings.mongodb_settings.partition] == lit(partition_value))