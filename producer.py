from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:29092")
producer.send("test_kafka", "test message".encode("utf-8"))
print("Message Sent")
producer.flush()
