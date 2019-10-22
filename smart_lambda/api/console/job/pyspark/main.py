import sys
import decimal
import datetime

from smart_lambda.infrastructure.di.bootstrap import Bootstrap
from smart_lambda.api.console.job.pyspark.app_resolver import AppResolver
from smart_lambda.api.console.job.pyspark.config import Config

def main():
    service_key = sys.argv[1]

    _config = Config.instance(service_key)
    Bootstrap.initialize(_config)

    app_service = _get_rawdata_service()
    app_service.save(datetime.datetime.now())

def _get_rawdata_service():
    return AppResolver.instance().get_rawdata_service()