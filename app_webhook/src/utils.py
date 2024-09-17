import json
import pika

from config import settings, logger

class RabbitMQConnection:
    """
    Class to manage the connection with RabbitMQ.
    
    Attributes:
        host (str): RabbitMQ server host.
        port (int): RabbitMQ server port.
        username (str): RabbitMQ access username.
        password (str): RabbitMQ access password.
        _connection (pika.BlockingConnection): The connection instance to RabbitMQ.
        _channel (pika.channel.Channel): The channel instance for RabbitMQ communication.
    """

    def __init__(self):
        """
        Initializes the RabbitMQConnection with the provided settings and establishes a connection.
        """
        self.host = settings.rabbit_host
        self.port = settings.rabbit_port
        self.username = settings.rabbit_username
        self.password = settings.rabbit_password
        self._connection = None
        self._channel = None
        self.connect()

    def connect(self):
        """
        Connects to RabbitMQ and creates a communication channel.
        
        Raises:
            Exception: If there is an error in establishing a connection.
        """
        try:
            connection_parameters = pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                credentials=pika.PlainCredentials(
                    username=self.username,
                    password=self.password
                )
            )
            self._connection = pika.BlockingConnection(connection_parameters)
            self._channel = self._connection.channel()
            logger.info("Connection to RabbitMQ established.")
        except Exception as e:
            logger.error(f"Error connecting to RabbitMQ: {e}")
            raise

    @property
    def channel(self):
        """
        Provides the current channel for communication with RabbitMQ.
        
        Returns:
            pika.channel.Channel: The channel for RabbitMQ communication.
        """
        return self._channel

    def close(self):
        """
        Closes the connection with RabbitMQ.
        """
        if self._connection:
            self._connection.close()
            logger.info("Connection to RabbitMQ closed.")

class RabbitMQPublisher:
    """
    Class to publish messages to RabbitMQ.
    
    Attributes:
        connection (RabbitMQConnection): An instance of RabbitMQConnection.
        exchange (str): RabbitMQ exchange name.
        routing_key (str): RabbitMQ routing key.
    """

    def __init__(self, connection: RabbitMQConnection):
        """
        Initializes the RabbitMQPublisher with a RabbitMQ connection.
        
        Args:
            connection (RabbitMQConnection): The connection instance to be used for publishing messages.
        """
        self.connection = connection
        self.exchange = settings.rabbit_exchange
        self.routing_key = settings.rabbit_routing_key

    def publish_message(self, body: dict):
        """
        Publishes a message to RabbitMQ.
        
        Args:
            body (dict): The message body to be published.
        
        Raises:
            Exception: If there is an error in publishing the message.
        """
        try:
            self.connection.channel.basic_publish(
                exchange=self.exchange,
                routing_key=self.routing_key,
                body=json.dumps(body),
                properties=pika.BasicProperties(
                    delivery_mode=2  # Make message persistent
                )
            )
            logger.info(f"Message published to RabbitMQ: {body}")
        except Exception as e:
            logger.error(f"Error publishing message: {e}")
            raise
