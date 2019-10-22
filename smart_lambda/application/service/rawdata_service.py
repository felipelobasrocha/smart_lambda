from smart_lambda.application.factory.application_factory import ApplicationFactory
from smart_lambda.data_domain.events.moving_data import MovingData

class RawDataService:

    _raw_data_access = None
    _app_factory = ApplicationFactory.instance()

    def __init__(self, raw_data_access, action):
        self._raw_data_access = raw_data_access
        self._event_trigger = self._app_factory.create_event()
        self._action = action

    def save(self, partition_value=None):
        data = self.get(partition_value)
        self._event_trigger.raise_event(MovingData, data, self._action)
        return data

    def get(self, partition_value=None):
        return self._raw_data_access.get(partition_value)