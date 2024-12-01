import contextlib
from typing import Generator

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.credentials import PlainCredentials


class RabbitMqConnectionFactory:
    def __init__(self, host: str, port: int, user: str, password: str) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password

        self.connection = None
        self.channel = None

    @contextlib.contextmanager
    def get_connection(self) -> Generator[BlockingChannel]:
        """
        Context manager that creates a connection to the RabbitMQ server
        :return :
        """
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.host,
                    port=self.port,
                    credentials=PlainCredentials(self.user, self.password)
                )
            )
            self.channel = self.connection.channel()
            yield self.channel
        finally:
            if self.connection and self.connection.is_open:
                self.connection.close()
                self.connection = None
                self.channel = None