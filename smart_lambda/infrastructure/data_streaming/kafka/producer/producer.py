from kafka import KafkaProducer

from smart_lambda.infrastructure.data_streaming.contracts.producer.iproducer import IProducer

class Producer(IProducer):

    def __init__(self, data_settings):
        self._data_settings = data_settings

    def send(self, domain_event, action):
        producer = KafkaProducer(bootstrap_servers=self._data_settings.domain_settings.kafka_settings.bootstrap_servers)
        data = {'data' : domain_event.domain}
        producer.send(self._data_settings.domain_settings.kafka_settings.topic, value=data)
        #producer.send('foobar', key=b'foo', value=b'bar')

    def raise_event(self, event, data_domain, callback):
        try:
            domain_event = event(data_domain)
            return self.save(domain_event, callback)
        except Exception as e:
            print "KafkaProducer error:" + str(e)