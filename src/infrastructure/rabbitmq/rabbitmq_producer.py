import json
from dataclasses import dataclass

import pika

from src.domain.events.message_producer import MessageProducer
from src.infrastructure.rabbitmq.RabbitMqConnectionFactory import RabbitMqConnectionFactory


@dataclass(frozen=True, eq=False)
class RabbitMQProducer(MessageProducer):
    factory: RabbitMqConnectionFactory

    def produce(self, topic: str, message) -> None:
        with self.factory.get_connection() as channel:
            channel.queue_declare(queue=topic)
            channel.basic_publish(
                exchange='',
                routing_key=topic,
                body=json.dumps(message).encode(),
                properties=pika.BasicProperties(delivery_mode=2)
            )