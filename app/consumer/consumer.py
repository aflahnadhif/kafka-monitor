from confluent_kafka import Consumer, KafkaException, KafkaError
import logging
import sys

logging.basicConfig(level=logging.INFO)

bootstrap_servers = 'localhost:9092,localhost:9093,localhost:9094'
topic_name = 'sample-topic'
group_id = 'sample-group'

base_path = "/Users/aflahnadhif/training-code/kafka-assignment2/keys/artifacts"
ca_file = f"{base_path}/ca.crt"
cert_file = f"{base_path}/python-consumer.crt"
key_file = f"{base_path}/python-consumer.key"

conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest',

    'security.protocol': 'ssl',
    'ssl.ca.location': ca_file,
    'ssl.certificate.location': cert_file,
    'ssl.key.location': key_file,

    'ssl.endpoint.identification.algorithm': 'none'
}

if __name__ == "__main__":
    consumer = None
    try:
        print("Initializing Confluent Kafka Consumer...")
        consumer = Consumer(conf)
        consumer.subscribe([topic_name])

        print(f"\nSuccessfully subscribed. Listening for messages on topic '{topic_name}'...")
        while True:
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f"Consumed: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        print("\nStopping consumer.")
    finally:
        if consumer:
            consumer.close()
