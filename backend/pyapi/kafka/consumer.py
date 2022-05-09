from kafka import KafkaConsumer
import msgpack
import json
import logging

logging.basicConfig(level=logging.WARNING)

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    api_version=(2, 0, 2),
    bootstrap_servers="127.0.0.1:9092",
    request_timeout_ms=5000,
    auto_offset_reset="latest",
    enable_auto_commit=False,
)

consumer.subscribe(["test3", "test2"])


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print(
        f"Consumed: {message.value} on {message.topic}"
        # "%s:%d:%d: key=%s value=%s"
        # % (message.topic, message.partition, message.offset, message.key, message.value)
    )
consumer2 = KafkaConsumer(
    api_version=(2, 0, 2),
    bootstrap_servers="127.0.0.1:9092",
    request_timeout_ms=5000,
    auto_offset_reset="earliest",
    enable_auto_commit=False,
)
