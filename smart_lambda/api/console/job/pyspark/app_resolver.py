from smart_lambda.infrastructure.di.factory import Factory

class AppResolver:

    def __init__(self):
        self._factory = Factory()

    def get_rawdata_service(self):
        return self._factory.create("RawDataService")

    _instance = None

    @staticmethod
    def instance():
        if AppResolver._instance is None:
            _instance = AppResolver()
        return _instance
