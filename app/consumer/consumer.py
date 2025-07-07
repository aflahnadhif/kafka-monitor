from kafka import KafkaConsumer
import json

def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

consumer = KafkaConsumer(
    'sample-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='sample-group',
    value_deserializer=json_deserializer
)

if __name__ == "__main__":
    for message in consumer:
        data = message.value
        print(f"Consumed: {data}")
        # Process the message here