from smart_lambda.infrastructure.events.event_manager import EventManager

class ApplicationFactory:

    _components = dict()

    def __init__(self):
        pass

    def create_event(self):
        return EventManager.instance()        

    _instance = None

    @staticmethod
    def instance():
        if ApplicationFactory._instance is None:
            _instance = ApplicationFactory()
        
        return _instance            