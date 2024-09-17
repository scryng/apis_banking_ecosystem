import logging
import logging.config
import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    Constructor method of class Config.
    The Config class inherits from BaseSettings.

    Attributes:
        api_title (str): Title of the API.
        api_version (str): Version of the API.
        api_host (str): Host of the API (server address).
        api_port (int): Port of the API.
        api_description (str): Description of the API.
        rabbit_host (str): RabbitMQ host.
        rabbit_port (str): RabbitMQ port.
        rabbit_username (str): RabbitMQ access username.
        rabbit_password (str): RabbitMQ access password.
        rabbit_queue (str): RabbitMQ queue name.
        rabbit_exchange (str): RabbitMQ exchange name.
        rabbit_routing_key (str): RabbitMQ routing key.
        database_url (str): Database URL.

    """

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    api_title: str
    api_version: str
    api_host: str
    api_port: int
    api_description: str
    rabbit_host: str
    rabbit_port: str
    rabbit_username: str
    rabbit_password: str
    rabbit_queue: str
    database_url: str


settings = Config()

config_path = os.path.join(os.path.dirname(__file__), 'logging.ini')

logging.config.fileConfig(config_path)
logger = logging.getLogger(f'{settings.api_title} - Logs')
