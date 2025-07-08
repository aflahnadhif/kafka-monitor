from confluent_kafka import Producer
import json
import time
import random
import socket

bootstrap_servers = 'localhost:9092,localhost:9093,localhost:9094'
topic_name = 'sample-topic'

base_path = "/Users/aflahnadhif/training-code/kafka-assignment2/keys/artifacts"
ca_file = f"{base_path}/ca.crt"
cert_file = f"{base_path}/python-producer.crt"
key_file = f"{base_path}/python-producer.key"

conf = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': socket.gethostname(),

    'security.protocol': 'ssl',
    'ssl.ca.location': ca_file,
    'ssl.certificate.location': cert_file,
    'ssl.key.location': key_file,

    'ssl.endpoint.identification.algorithm': 'none'
}

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")

if __name__ == "__main__":
    producer = None
    try:
        print("Initializing Confluent Kafka Producer...")
        producer = Producer(conf)

        print("Producer connected. Starting to send messages...")
        while True:
            data = {
                'timestamp': time.time(),
                'value': random.randint(1, 100)
            }

            payload = json.dumps(data).encode('utf-8')

            producer.produce(topic_name, value=payload, callback=acked)
            print(f"Producing: {data}")

            producer.poll(0)

            # time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping producer...")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if producer:
            print("Flushing final messages...")
            producer.flush()
