# Playground

This repository is a collection of small projects and experiments.

## Contents

*   **[rabbitmq/producer-consumer/](./rabbitmq/producer-consumer/)**: Contains a simple producer-consumer implementation using Python.
    *   [`consumer.py`](./rabbitmq/producer-consumer/consumer.py): The consumer script.
    *   [`producer.py`](./rabbitmq/producer-consumer/producer.py): The producer script.
*   **[rabbitmq/publish-subscribe/](./rabbitmq/publish-subscribe/)**: Contains a basic publish-subscribe implementation.
    *   [`publisher.py`](./rabbitmq/publish-subscribe/publisher.py): The publisher script.
    *   [`subscriber.py`](./rabbitmq/publish-subscribe/subscriber.py): The subscriber script.

## Dependencies

The project uses `uv` for dependency management.  You can install the dependencies using:

```bash
uv venv
source .venv/bin/activate
uv sync
```