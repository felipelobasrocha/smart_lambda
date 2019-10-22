from smart_lambda.infrastructure.data_access.contracts.iraw_data_access import IRawDataAccess

class RawDataAccess(IRawDataAccess):

    def __init__(self, data_settings, hive):
        self._data_settings = data_settings
        self._hive = hive

    def get(self, partition_value=None):      
        data = self._data_domain()
        if partition_value!=None:
            data = data.where(data[self._data_settings.hive_settings.partition] == partition_value)
        return data

    def save(self, domain_event, action):
        self._hive.create(domain_event.domain, self._data_settings.hive_settings.table, type_pattern, self._data_settings.hive_settings.partition, self._data_settings.hive_settings.location, self._data_settings.spark.sql)
        action(domain_event.domain, self._data_settings.hive_settings.table)

    def _data_domain():
        return self._data_settings.spark.session.table(self._data_settings.hive_settings.table)

    def raise_event(self, event, data_domain, callback):
        try:
            domain_event = event(data_domain)
            return self.save(domain_event, callback)
        except Exception as e:
            print "HiveRawDataAccess error:" + str(e)