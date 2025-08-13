## Running the RabbitMQ Server

The producer-consumer and publish-subscribe examples use RabbitMQ. To run the RabbitMQ server locally with Docker, use the following command:

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
```

This command will start a RabbitMQ server with the management UI accessible at `http://localhost:15672`.

## Dependencies

The project uses `uv` for dependency management.  You can install the dependencies using:

```bash
uv venv
source .venv/bin/activate
uv sync
```