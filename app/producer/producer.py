from kafka import KafkaProducer
import json
import time
import random

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'],
    value_serializer=json_serializer
)

if __name__ == "__main__":
    while True:
        # Generate sample data
        data = {
            'timestamp': time.time(),
            'value': random.randint(1, 100)
        }
        
        # Send data to Kafka topic
        producer.send('sample-topic', value=data)
        print(f"Produced: {data}")
        
        # Wait before sending next message
        # time.sleep(1)