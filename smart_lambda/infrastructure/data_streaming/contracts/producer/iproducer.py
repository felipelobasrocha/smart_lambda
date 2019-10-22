from abc import ABCMeta, abstractmethod

class IProducer:

    @abstractmethod
    def send(self, domain_event, action): pass    