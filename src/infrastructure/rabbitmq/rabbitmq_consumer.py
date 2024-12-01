from dataclasses import dataclass
from typing import Callable

from src.domain.events.message_consumer import MessageConsumer
from src.infrastructure.rabbitmq.RabbitMqConnectionFactory import RabbitMqConnectionFactory


@dataclass(frozen=True, eq=False)
class RabbitMQConsumer(MessageConsumer):
    factory: RabbitMqConnectionFactory

    def consume(self, topic: str, callback: Callable) -> None:
        with self.factory.get_connection() as channel:
            channel.queue_declare(queue=topic)

            def on_message(channel, method, properties, body):
                callback(body)

            channel.basic_consume(
                queue=topic,
                on_message_callback=on_message,
                auto_ack=True,
            )
            channel.start_consuming()
