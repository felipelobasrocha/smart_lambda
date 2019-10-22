from example.infrastructure.di.factory import Factory

class ContainerResolver:

    _factory = Factory()

    def __init__(self):
        pass

    _instance = None

    @staticmethod
    def instance():
        if ContainerResolver._instance is None:
            _instance = ContainerResolver()
        return _instance
