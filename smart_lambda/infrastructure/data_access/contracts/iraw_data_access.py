from abc import ABCMeta, abstractmethod

class IRawDataAccess:

    @abstractmethod
    def get(self, partition_value): pass

    @abstractmethod
    def save(self, domain_event, action): pass