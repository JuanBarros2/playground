import pika
import time


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def main():
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange='topic', exchange_type='fanout')

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='topic', queue=queue_name)
        channel.basic_consume(
            queue=queue_name, auto_ack=True, on_message_callback=callback
        )
        channel.start_consuming()


if __name__ == "__main__":
    main()
