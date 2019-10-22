import os
import sys

from factory import Factory

from smart_lambda.application.service.rawdata_service import RawDataService

from smart_lambda.data_domain.model.hive import Hive

from smart_lambda.infrastructure.data_processing.spark.hive.spark import Spark
from smart_lambda.infrastructure.data_processing.spark.hive.actions import write as Write
from smart_lambda.infrastructure.data_processing.spark.mongodb.actions import write as WriteMongoDB
from smart_lambda.infrastructure.data_processing.spark.hive.actions import save_as_table

from smart_lambda.infrastructure.events.event_manager import EventManager
from smart_lambda.data_domain.events.moving_data import MovingData

from smart_lambda.infrastructure.data_access.contracts.iraw_data_access import IRawDataAccess
from smart_lambda.infrastructure.data_access.hive.raw_data_access import RawDataAccess as RawHiveDataAccess
from smart_lambda.infrastructure.data_access.mongodb.raw_data_access import RawDataAccess as RawMongoDataAccess

from smart_lambda.infrastructure.data_streaming.contracts.producer.iproducer import IProducer
from smart_lambda.infrastructure.data_streaming.kafka.producer.producer import Producer as KafkaProducer

class Bootstrap:

    def __init__(self, config):
        self._config = config
        self._data_settings = type('data_config', 
                                    (object,), 
                                    {
                                        'spark' : Spark.instance(self._config.name),
                                        'hive_settings' : self._config.domain_settings.hive_settings,
                                        'mongodb_settings': self._config.domain_settings.mongodb_settings
                                    }
                                )        
        self._factory = Factory.instance()
        self._event_manager = EventManager.instance()

    def _register(self):
        source_dataaccess = self._get_source_data_access()
        self._register_infrastructure(source_dataaccess)
        self._register_app_services(source_dataaccess)
        self._register_events()

    def _register_infrastructure(self, source_dataaccess):
        self._factory.register(IRawDataAccess, source_dataaccess)

    def _register_app_services(self, source_dataaccess):
        self._factory.register("RawDataService", RawDataService(source_dataaccess, save_as_table.action))

    def _register_events(self):
        destination_dataaccess = self._get_destination_data_access()
        self._event_manager.register(MovingData, KafkaProducer(self._data_settings))
        self._event_manager.register(MovingData, destination_dataaccess)

    def _get_source_data_access(self):
        if self._config.domain_settings.source.name.upper() == "MONGODB":
            return RawMongoDataAccess(self._data_settings)
        else:
            return RawHiveDataAccess(self._data_settings)

    def _get_destination_data_access(self):
        if self._config.domain_settings.destination.name.upper() == "MONGODB":
            return RawMongoDataAccess(self._data_settings)
        else:
            return RawHiveDataAccess(self._data_settings, Hive(DDLCommand()))            

    @staticmethod
    def initialize(config):
        Bootstrap(config)._register()