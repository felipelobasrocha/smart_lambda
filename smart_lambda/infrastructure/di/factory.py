
class Factory():

    _components = dict()

    def __init__(self):
        pass

    def create(self, type):
        return self._components[type]

    def register(self, type, instance):
        if type == None:
            raise Exception(str(type))

        if instance == None:
            raise Exception(str(instance))

        self._components[type] = instance

        return self

    _instance = None

    @staticmethod
    def instance():
        if Factory._instance is None:
            _instance = Factory()
        
        return _instance
