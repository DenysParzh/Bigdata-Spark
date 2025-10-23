import json
import time

from kafka import KafkaProducer

from configuration import BOOTSTRAP_SERVERS, TOPIC


def serializer(data):
    return json.dumps(data).encode('utf-8')


def produce(producer):
    for row_i in range(100):
        data = {'row_iteration': row_i}
        producer.send(TOPIC, data)
        print(f'Sent to Kafka: {row_i}')

        time.sleep(2)


def main():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=serializer
    )

    produce(producer)


if __name__ == '__main__':
    main()
