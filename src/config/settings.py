from enum import Enum

from pydantic import BaseSettings


class QueueEnum(str, Enum):
    QUEUE_AAA = "QUEUE_AAA"
    QUEUE_BBB = "QUEUE_BBB"
    QUEUE_CCC = "QUEUE_CCC"


class Base(BaseSettings):
    RABBITMQ_DEFAULT_USER: str = 'user'
    RABBITMQ_DEFAULT_PASS: str = 'password'
    RABBITMQ_LOCAL_HOST_NAME: str = 'rabbit'
    RABBITMQ_LOCAL_PORT: int = 5672
    RABBITMQ_QUEUE: str = 'test_queue'

    CLIENT_ORIGIN: str = 'http://localhost:3000'


setting = Base()
RABBIT_URL = f'amqp://{setting.RABBITMQ_DEFAULT_USER}:' \
             f'{setting.RABBITMQ_DEFAULT_PASS}@' \
             f'{setting.RABBITMQ_LOCAL_HOST_NAME}:' \
             f'{setting.RABBITMQ_LOCAL_PORT}/'
