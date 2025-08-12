import pika


def main():
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="task_hello", durable=True)
        while True:
            message = input("Digite sua mensagem:")
            channel.basic_publish(
                exchange="",
                routing_key="task_hello",
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=pika.DeliveryMode.Persistent
                ),
            )
            print(f" [x] Sent '{message}'")
            if message == "sair":
                break


if __name__ == "__main__":
    main()
