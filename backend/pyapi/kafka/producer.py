from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging

logging.basicConfig(level=logging.WARNING)

print("hey")

producer = KafkaProducer(
    api_version=(2, 0, 2),
    client_id="py-producer",
    bootstrap_servers="127.0.0.1:9092",
    max_block_ms=20000,
)

producer2 = KafkaProducer(
    api_version=(2, 0, 2),
    client_id="py-producer",
    bootstrap_servers=["127.0.0.1:9093"],
)
try:
    for x in range(5):

        producer.send(
            topic="test3",
            key=bytes("hey", encoding="utf8"),
            value=bytes(f"message{x} produced on test3", encoding="utf8"),
        )

        producer2.send(
            topic="test2",
            key=bytes("hey", encoding="utf8"),
            value=bytes(f"message{x} produced on test2", encoding="utf8"),
        )
except Exception as e:
    print(e)
print("hey2")

# Asynchronous by default
# future = producer.send("test2", b"raw_bytes")
# future2 = producer2.send("test3", b"raw_bytes")

# # Block for 'synchronous' sends
# try:
#     print("hey")
#     record_metadata = future.get(timeout=10)
# except KafkaError:
#     print("hey")
#     # Decide what to do if produce request failed...
#     log.exception()
#     pass

# # Successful result returns assigned partition and offset
# print(record_metadata.topic)
# print(record_metadata.partition)
# print(record_metadata.offset)
# print("here here2")
# # produce keyed messages to enable hashed partitioning
# producer.send("test2", key="foo", value="bar")

# print("\nhere here\n")

# # encode objects via msgpack
# producer = KafkaProducer(value_serializer=msgpack.dumps)
# producer.send("msgpack-topic", {"key": "value"})

# # produce json messages
# producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode("ascii"))
# producer.send("json-topic", {"key": "value"})

# produce asynchronously
for _ in range(100):
    producer.send("test2", b"msg")


# def on_send_success(record_metadata):
#     print(record_metadata.topic)
#     print(record_metadata.partition)
#     print(record_metadata.offset)


# def on_send_error(excp):
#     log.error("I am an errback", exc_info=excp)
#     # handle exception


# # produce asynchronously with callbacks
# producer.send("test2", b"raw_bytes").add_callback(on_send_success).add_errback(
#     on_send_error
# )

# # block until all async messages are sent
# producer.flush()

# # configure multiple retries
# producer = KafkaProducer(retries=5)
