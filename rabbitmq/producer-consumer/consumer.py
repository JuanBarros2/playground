import pika
import time


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    time.sleep(3)


def main():
    prefetch_count = input("Prioridade do worker: ")
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="task_hello", durable=True)
        # Durable irá persistir a fila mesmo quando o servidor cair

        channel.basic_qos(prefetch_count=int(prefetch_count))
        channel.basic_consume(
            queue="task_hello", auto_ack=True, on_message_callback=callback
        )
        channel.start_consuming()


if __name__ == "__main__":
    main()
