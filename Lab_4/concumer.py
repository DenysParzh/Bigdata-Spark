import json
import time

from kafka import KafkaConsumer

from configuration import BOOTSTRAP_SERVERS, TOPIC


def deserializer(data):
    return json.loads(data.decode('utf-8'))


def consume(consumer):
    for message in consumer:
        data = message.value
        print(data)

        time.sleep(3)


def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        value_deserializer=deserializer
    )

    consume(consumer)


if __name__ == '__main__':
    main()
