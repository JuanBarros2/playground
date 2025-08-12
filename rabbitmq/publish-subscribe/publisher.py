import pika


def main():
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange="topic", exchange_type="fanout")
        while True:
            message = input("Digite sua mensagem:")
            channel.basic_publish(
                exchange="topic",
                routing_key='',
                body=message,
            )
            print(f" [x] Sent '{message}'")
            if message == "sair":
                break


if __name__ == "__main__":
    main()
