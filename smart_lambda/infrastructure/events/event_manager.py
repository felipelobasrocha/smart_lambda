
class EventManager:
    events = dict()
    subscribers = []

    def register(self, event, subscriber):
        key = str(event)

        if key not in self.events:
            self.subscribers.append(subscriber)
            self.events[key] = self.subscribers
        else:
            self.events[key].append(subscriber)
        
        return self.events[key]

    def raise_event(self, event, domain, callback=None):
        if self.events[str(event)] is None:
            return
            
        subscribers = self.events[str(event)]

        for subscriber in subscribers:
            subscriber.raise_event(event, domain, callback)

    _instance = None

    @staticmethod
    def instance():
        if EventManager._instance == None:
            _instance = EventManager()
        return _instance